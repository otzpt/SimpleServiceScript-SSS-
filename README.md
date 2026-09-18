# SimpleServiceScript(SSS)

A simple **CLI** tool made in ``python`` to **activate/deactivate/restart/status** 
of services on linux

## Features

- **start**: starts a specific service

- **stop**: stops a specific service

- **restart**: restarts a specific service

- **status**: gets status on a specific service

## Requirements

- **Linux**

- **systemd** or **runit**

- **python 3**

## AI usage notice

The Code itself is **written entirely by humans** AI was used as a **tool for learning** and **never** to write code
the only thing AI did that it had acess to code was to find bugs and list them in `bugs.md`, that is also the reason
`.claude` is in the .gitignore

## Notice

For now `SimpleServiceScripts-SSS-` only supports **systemD** and **Runit** (Windows support soon)
So make sure your Linux distro use either **Runit** or **SystemD**

## How to use

First make sure you have python3 installed
after that you are going to:
```bash
git clone https://github.com/otzpt/SimpleServiceScript-SSS-
```
to the folder you want it at, then you are going to cd to the **SSS** folder
and then execute:
```bash
python3 main.py
```
or
```bash
python main.py
```
