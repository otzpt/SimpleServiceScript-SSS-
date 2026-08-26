import subprocess
import os

def activateProcessR():
    service = input("insert the service you want to start: ")
    output = subprocess.run(["sv", "status", service], capture_output=True)
    status = output.stdout.decode().strip()

    # see if service is stoped
    # or running if its stoped
    # proceds with start
    if "down" in status:
        subprocess.run(["sv", "start", service])
        print(f"service {service} started")
    else:
        print(f"{service} is already running")

def deactivateProcessR():
    # gets input and gets status of the service/process
    service = input("insert the name of the service/process you want to deactivate: ")
    output = subprocess.run(["sv", "status", service], capture_output=True)
    status = output.stdout.decode().strip()
    
    # checks if process is already stoped
    # if not stops the service/process
    # idk what to call it
    if "run" in status:
        subprocess.run(["sv", "stop", service])
        print(f"deactivated {service}")
    else:
        print(f"{service} is not running")

def restartProcessR():
    service = input("name of service: ")
    # restarts the process with systemclt
    output = subprocess.run(["sv", "restart", service])
    
    print("service/process restarted")

def processStatusR():
    # asks user for the process they want
    # to get status from
    service = input("name of service: ")
    output = subprocess.run(["sv", "status", service], capture_output=True)# gets status using systemclt
    status = output.stdout.decode().strip()
    print(status)
