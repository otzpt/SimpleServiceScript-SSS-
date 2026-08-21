import subprocess
import os

def activateProcess():
    process = input("insert here the service/process name you want to activate: ")
    output = subprocess.run(["systemctl", "--user", "status", process], capture_output=True)
    status = output.stdout.decode().strip()

    if "inactive" in status:
        subprocess.run(["systemctl", "--user", "start", process])
        print(f"service/process {process} started")
    else:
        print(f"{process} is already running")

def deactivateProcess():
    process = input("insert the name of the service/process you want to deactivate: ")
    output = subprocess.run(["systemctl", "--user", "status", process], capture_output=True)
    status = output.stdout.decode().strip()

    if "active" in status:
        subprocess.run(["systemctl", "--user", "stop", process])
        print(f"deactivated {process}")
    else:
        print(f"{process} is not running")

def restartProcess():
    process = input("name of process/service: ")
    output = subprocess.run(["systemctl", "--user", "restart", process])
    
    print("service/process restarted")

def processStatus():
    process = input("name of process/service: ")
    output = subprocess.run(["systemctl", "--user", "status", process], capture_output=True)
    status = output.stdout.decode().strip()
    print(status)

print("[1] activate service")
print("[2] deactivate service")
print("[3] restart service")
print("[4] service status")
print("[0] exit")

opt = input("option here: ")

if opt == "1":
    os.system("clear")
    activateProcess()
elif opt == "2":
    os.system("clear")
    deactivateProcess()
elif opt == "3":
    os.system("clear")
    restartProcess()
elif opt == "4":
    os.system("clear")
    processStatus()
elif opt == "0":
    os.system("clear")
    exit(0)
else:
    print("invalid option")
