# Known bugs

## win.py

- `serviceRestart()`, STOPPED branch: after starting the service, if the
  status check shows RUNNING (the start succeeded), it prints
  "restart failed". The message is inverted for that case.

- `status()`: the per-line loop returns on the very first line regardless of
  whether it contains "STATE" (the `else` branch of the `if "STATE" in line`
  check returns 3 unconditionally). Since `sc query` output lists
  SERVICE_NAME and TYPE before STATE, the loop exits before ever reaching
  the state line, so the intended STATE line is effectively never read.

- `status()`: once a line containing "STATE" is found, the RUNNING/STOPPED
  check is done with `in output` (the whole multi-line output) instead of
  `in line`. This defeats the comment's stated purpose, checking line by
  line so a service name that happens to contain "RUNNING" doesn't get
  misread as the state.

- `serviceRestart()`, service-stopped branch: the condition is
  `elif 1 == status`, comparing the `status` function object itself to 1
  instead of calling `status(service)`. This is always false, so the whole
  branch that restarts a stopped service is unreachable.

- `deactivateService()`: there's no branch for when the service isn't
  running (`output` other than 0). The function silently does nothing and
  prints no message, unlike `activateProcess()` which reports on every
  status.
## fixed

- `activateProcess()`: the else branch after the STOPPED check assumes
  anything that isn't STOPPED means the service is running. A bad service
  name or a query error falls into this branch too and gets misreported
  as "service is already running" instead of a real error.
## fixed

## sysD.py

- `status()`: `subprocess.run` is called without `text=True`, so `.stdout` is
  `bytes`. It's then compared against the string literals `"active"` and
  `"inactive"`, which never match. The function always falls through to the
  `else` branch and returns 2, regardless of the service's real state.

- `status()`: `is-active` is run with `check=True`. systemctl exits non-zero
  for an inactive or failed service, so instead of returning 1/2 cleanly the
  call raises `CalledProcessError` before the `if output ==` checks run.

- `deactivateProcess()`: the message "{service} failed to start" is printed
  after a stop attempt succeeds status-wise, describing a start failure
  instead of a stop failure.

## runit.py

- `activateProcessR()` and `deactivateProcessR()`: the status checks use a
  bare substring match (`"down" in status`, `"run" in status`) against the
  raw `sv status` output instead of parsing the leading state word. A
  service name that itself contains "run" or "down" can make the check
  match the name rather than the actual state.

- None of the `sv start` / `sv stop` / `sv restart` calls use `check=True`
  or re-check status afterward, unlike the equivalent functions in
  `sysD.py` and `win.py`. `activateProcessR()`, `deactivateProcessR()`, and
  `restartProcessR()` all print a success message unconditionally, even if
  the underlying `sv` command failed or the service never changed state.
