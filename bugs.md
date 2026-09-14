# Known bugs

## win.py

- `serviceRestart()`, STOPPED branch: after starting the service, if the
  status check shows RUNNING (the start succeeded), it prints
  "restart failed". The message is inverted for that case.
## fixed

- `activateProcess()`: the else branch after the STOPPED check assumes
  anything that isn't STOPPED means the service is running. A bad service
  name or a query error falls into this branch too and gets misreported
  as "service is already running" instead of a real error.
## fixed
