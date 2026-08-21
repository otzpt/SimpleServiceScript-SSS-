import subprocess
import os

# IMPORTANT!!
# ALWAYS TRY TO USE "--user"
# FOR SERVICE/PROCESS
# PEOPLE COULD HAVE MULTIPLE USERS
# PLUS IS BETTER UX AND GOOD USE OF FREE WILL

def activateProcess():
    process = input("insert here the service/process name you want to activate: ")
    output = subprocess.run(["systemctl", "--user", "status", process], capture_output=True)
    status = output.stdout.decode().strip()

    # see if service is stoped
    # or running if its stoped
    # proceds with start
    if "inactive" in status:
        subprocess.run(["systemctl", "--user", "start", process])
        print(f"service/process {process} started")
    else:
        print(f"{process} is already running")

def deactivateProcess():
    # gets input and gets status of the service/process
    process = input("insert the name of the service/process you want to deactivate: ")
    output = subprocess.run(["systemctl", "--user", "status", process], capture_output=True)
    status = output.stdout.decode().strip()
    
    # checks if process is already stoped
    # if not stops the service/process
    # idk what to call it
    if "active" in status:
        subprocess.run(["systemctl", "--user", "stop", process])
        print(f"deactivated {process}")
    else:
        print(f"{process} is not running")

def restartProcess():
    process = input("name of process/service: ")
    # restarts the process with systemclt
    output = subprocess.run(["systemctl", "--user", "restart", process])
    
    print("service/process restarted")

def processStatus():
    # asks user for the process they want
    # to get status from
    process = input("name of process/service: ")
    output = subprocess.run(["systemctl", "--user", "status", process], capture_output=True)# gets status using systemclt
    status = output.stdout.decode().strip()
    print(status)

# improvised main menu and function calling
# i might make a GUI version of
# this altough i like how cli looks
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
