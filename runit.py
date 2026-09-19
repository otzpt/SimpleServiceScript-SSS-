import subprocess

# please
# always use check = True
# in subprocess.run or if you dont want to
# use check = False and use try except

def status(service):
    output = subprocess.run(["sv", "status", service],check = True, capture_output=True, text=True).stdout
    if "run" in output:
        return 0
    elif "down" in output:
        return 1
    else:
        return 2

def activateProcessR():
    service = input("insert the service you want to start: ")
    output = status(service)

    # see if service is stoped
    # or running if its stoped
    # proceds with start
    if 1 == output:
        subprocess.run(["sv", "start", service], check = True)
        # recheck status so we know if the service actully started or not
        output = status(service)
        if 0 == output:
            print(f"{service} started")
        elif 1 == output:
            print(f"{service} failed to start, make sure you have sudo")
        else:
            print("make sure the tool as sudo permissions, service name is correct, service exists")
    elif 0 == output:
        print(f"{service} is already running")
    else:
        print("make sure the tool as sudo permissions, service name is correct, service exists")

def deactivateProcessR():
    # gets input and gets status of the service/process
    service = input("insert the name of the service/process you want to deactivate: ")
    output = status(service)

    # checks if process is already stoped
    # because if its stopped and we try to stop it wont do anything
    # but if its on we need to do something
    # if not stops the service
    if 0 == output:
        subprocess.run(["sv", "stop", service], check=True)
        # simple error handling
        if output == 1:
            print(f"deactivated {service}")
        elif output == 0:
            print(f"{service} failed to stop, make sure you have sudo")
        else:
            print("make sure the tool as sudo permissions, service name is correct, service exists")
    else:
        print(f"{service} is already stopped")

def restartProcessR():
    service = input("name of service: ")
    subprocess.run(["sv", "restart", service], check=True)
    output = status(service)

    if output == 0:
       print(f"{service} restarted")
    elif output == 1:
       print(f"{service} failed tpo restart, make sure you started this program with sudo")
    else:
        print("make sure the tool as sudo permissions, service name is correct, service exists")

def processStatusR():
    # asks user for the process they want
    # to get status from
    service = input("name of service: ")
    output = status(service)

    if output == 0:
        print(f"{service} is running")
    elif output == 1:
        print(f"{service} is stopped")
    else:
        print("honestly i dont know bro;")
        print("make sure the tool as sudo permissions, service name is correct, service exists")
