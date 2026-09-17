import subprocess
import time

# IMPORTANT!!
# ALWAYS TRY TO USE "--user"
# FOR SERVICE/PROCESS
# PEOPLE COULD HAVE MULTIPLE USERS
# PLUS IS BETTER UX AND GOOD USE OF FREE WILL

def status(service):
    output = subprocess.run(["systemctl", "--user", "is-active", service], capture_output = True, check = True).stdout

    if output == "active":
        return 0
    elif output == "inactive":
        return 1
    else:
        # 2 means either there is no service with that name, service doesnt exits,
        # not enough privileges, or the command failed for some reason
        # this is like a second wall of defense if check = True fails
        # idk how to explain this that well
        return 2


def activateProcess():
    service = input("insert here the service name you want to activate: ")
    output = status(service)

    # see if service is stoped
    # or running if its stoped
    # proceds with start

    if output == 1:
        print("service is starting...")
        time.sleep(3)

        subprocess.run(["systemctl", "--user", "start", service], check=True)
        output = status(service)
        if output == 0:
            print(f"service/process {service} started")
        elif output == 1:
            print(f"service {service} failed to start")
            print("this might happen because this program needs sudo")
        else:
            print("make sure you have ran this program with sudo, inserted the correct name or if service exists")
    elif output == 0:
        print(f"{service} is already running")
    else:
        print("make sure you have ran this program with sudo, inserted the correct name or if service exists")

def deactivateProcess():
    # gets input and gets status of the service/process
    service = input("insert the name of the service you want to deactivate: ")
    output = status(service)

    # checks if process is already stoped
    # if not stops the service/process
    # idk what to call it
    if output == 0:
        subprocess.run(["systemctl", "--user", "stop", service], check = True)
        output = status(service)
        if output == 1:
            print(f"deactivated {service}")
        elif output == 0:
            print(f"{service} failed to start make sure you started this program with sudo")
        elif output == 2:
            print("make sure you have ran this program with sudo, inserted the correct name or if service exists")
    else:
        print(f"{service} is not running")

def restartProcess():
    service = input("name of the service: ")
    # restarts the process with systemclt
    try:
        subprocess.run(["systemctl", "--user", "restart", service], check = True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to restart {service}; Exit code: {e.returncode}")
    else:
        print(f"{service} restarted successfully")

def processStatus():
    # asks user for the process they want
    # to get status from
    service = input("what service do you want to check on: ")
    print("0 means running, 1 means stoped, 2 means anything else(not enough permissions, service not found, wrong name, etc...)")
    print("checking...")
    time.sleep(2)
    output = status(service)
    print(f"{service} status: {output}")

# main menu was moved to menu.py
# menu.py became main.py btw
