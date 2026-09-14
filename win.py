import subprocess
import time

def status(service):
    output = subprocess.run(["sc", "query", service], capture_output = True, text = True, check = True).stdout
    # checks line by line for "state" substring so it doesnt flag the service name
    # as the state for example if you have my_running_service or smt with RUNNING in
    # it would get flagged without this
    for line in output.splitlines():
        if "STATE" in line:
            if "RUNNING" in output:
                return 0
            elif "STOPPED" in output:
                return 1
            else:
                return 2
        else:
            return 3

def activateProcess():
    service = input("What is the service you want to start: ")
    output = status(service)

    if 1 == output:
        print("service starting...")
        subprocess.run(["sc", "start", service], check = True)
        time.sleep(2)
        # recheck service status
        output = status(service)
        # obvious but checks if service actually started
        if 0 == output:
            print("service started")
        elif 1 == output:
            print("service failed to start")
    elif 0 == output:
        print("service is alredy running")
    elif 2 == output:
        print("i honestly dont know most likely you typed in the wrong name")
        print("or service doesn't exist")
    elif 3 == output:
        print("program couldn't grasp service state most likely service typed doesnt exist")

def deactivateService():
    service = input("what service do you want to stop: ")
    output = status(service)

    if 0 == output:
        subprocess.run(["sc", "stop", service], check = True)
        # recheck
        output = status(service)
        if 0 == output:
            print("service failed to stop")
        elif 1 == output:
            print("service stopped")
        else:
            print("IDK")

def serviceRestart():
    service = input("what service do you want to restart: ")
    output = status(service)

    # if the service is running
    if 0 == output:
        subprocess.run(["sc", "stop", service], check = True)
        print(f"{service} is stopping...")
        time.sleep(5)
        output = status(service)
        # quick check
        if 0 == output:
            print("service failed to stop")

        subprocess.run(["sc", "start", service], check = True)
        print(f"{service} is starting...")
        output = status(service)
        # another quick check
        if 1 == output:
            print("service failed to start")
    # if the service is stopped
    elif 1 == status:
        subprocess.run(["sc", "start", service], check = True)
        print(f"{service} is starting...")
        time.sleep(5)
        output = status(service)
        # quick check again
        if 1 == output:
            print("service failed to start")
        # stops the service and rechecks status
        subprocess.run(["sc", "stop", service], check = True)
        print(f"{service} is stopping...")
        output = status(service)
        if 0 == output:
            print("service failed to stop")
        # small warning its obvious but as a coding begginer i like to comment
        print("if you wanted the service to start use start in menu options \n (restart return's service to state that it was before restart)")

def serviceStatus():
    # obvious
    service = input("what is the service you want to check the status on: ")
    print("!!NOTICE: 0 means running; 1 means stopped; 2 means something else i dont know; 3 means unable to get status!!")
    output = status(service)
    print(output)
