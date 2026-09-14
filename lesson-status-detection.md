# Lesson: don't substring-match a status report

## The bug

`sysD.py` currently does this to check if a service is running:

```python
output = subprocess.run(["systemctl", "--user", "status", process], capture_output=True)
status = output.stdout.decode().strip()

if "active" in status:
    ...
```

`systemctl status` prints a whole human-readable block, meant for a person to
read in a terminal, not for a program to search through. Somewhere in that
block is a line like:

```
Active: active (running) since ...
```

or

```
Active: inactive (dead) since ...
```

The word `"inactive"` **contains** the word `"active"` as a substring. So
`"active" in status` is `True` in *both* cases. The check can never tell the
two states apart, it always matches.

This is exactly why substring-matching free-form text is fragile: the check
isn't wrong because of a typo, it's wrong because the shape of the data makes
"contains X" ambiguous. The fix isn't a smarter substring, it's not parsing
free text at all.

## The fix: ask for just the state, not a report

`systemctl` has a subcommand built for exactly this, no report, just the
answer:

```bash
systemctl is-active nginx
```

This prints one word: `active`, `inactive`, `failed`, `activating`,
`deactivating`, or `unknown`, and nothing else. It also sets its exit code
to `0` only when the service is active, so you don't even have to read
stdout if you don't want to, a process's own return code already says it.

```python
result = subprocess.run(["systemctl", "--user", "is-active", process], capture_output=True)
is_running = result.returncode == 0
# or, if you want the exact word:
state = result.stdout.decode().strip()   # e.g. "active", "inactive", "failed"
```

No substring search, no ambiguity.

## What about runit?

`runit`'s `sv status` doesn't have a dedicated one-word twin the way
`systemctl` does, but its output puts the state as the very first word on
the line, e.g. `run: myservice: (pid 1234) 3600s` when up, or
`down: myservice: 5s, normally up` when down. That means you can anchor on
the *prefix* instead of searching anywhere in the string:

```python
status.startswith("run:")   # instead of "run" in status
status.startswith("down:")  # instead of "down" in status
```

This is narrower than "contains," so it can't accidentally match a word
that shows up somewhere else in the line.

**Don't take the exact wording above as gospel, check it yourself**: run
`sv status <some-real-service>` on your own machine and look at what it
actually prints before you anchor on `"run:"`. The whole point of this
lesson is "verify the actual shape of the data instead of assuming," so
apply that here too rather than copy this file's example blindly.

## The general lesson

When a tool offers both a "report" command and a "just tell me the state"
command, prefer the second one for anything a program is going to branch on.
Reports are formatted for humans and can change wording between versions;
a dedicated state query is a stable, minimal contract. If no such command
exists, parsing free text is sometimes unavoidable, but then anchor on
something structural (a fixed prefix, a specific line, a delimiter) instead
of a bare substring search, and think about whether any other valid value
could contain your search string as a substring, the way `"inactive"`
contains `"active"`.
