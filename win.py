import subprocess
import time

def activateProcess():
    service = input("What is the service you want to start: ")
    output = subprocess.run(["sc", "query", service], capture_output = True, text = True)
    status = output.stdout.strip()
    print(status)

    if "STOPPED" in status:
        print("service starting...")
        subprocess.run(["sc", "start", service])
        time.sleep(2)
        # recheck service status
        output = subprocess.run(["sc", "query", service], capture_output = True, text = True)
        status = output.stdout.strip()
        # obvious but checks if service actually started
        if "RUNNING" in status:
            print("service started")
        else:
            print("service failed to start")
    else:
        print("service is alredy running")

def deactivateService():
    service = input("what service do you want to stop: ")
    output = subprocess.run(["sc", "query", service], capture_output=True, text = True)
    status = output.stdout.strip()

    if "RUNNING" in status:
        subprocess.run(["sc", "stop", service])
        # recheck
        output = subprocess.run(["sc", "query", service], capture_output=True, text = True)
        status = output.stdout.strip()
        if "RUNNING" in status:
            print("service failed to stop")
        elif "STOPPED" in status:
            print("service stopped")
        else:
            print("IDK")

def serviceRestart():
    service = input("what service do you want to restart: ")
    output = subprocess.run(["sc", "query", service], capture_output=True, text = True)
    status = output.stdout.strip()
    if "RUNNING" in status:
        subprocess.run(["sc", "stop", service])
        print(f"{service} is stopping...")
        time.sleep(5)
        output = subprocess.run(["sc", "query", service], capture_output=True, text = True)
        status = output.stdout.strip()
        if "RUNNING" in status:
            print("restart failed")
        subprocess.run(["sc", "start", service])
        print(f"{service} is starting...")
        output = subprocess.run(["sc", "query", service], capture_output=True, text = True)
        status = output.stdout.strip()
        if "STOPPED" in status:
            print("service failed start")
    elif "STOPPED" in status:
        subprocess.run(["sc", "start", service])
        print(f"{service} is starting...")
        time.sleep(5)
        output = subprocess.run(["sc", "query", service], capture_output=True, text = True)
        status = output.stdout.strip()
        if "RUNNING" in status:
            print("restart failed")
        subprocess.run(["sc", "stop", service])
        print(f"{service} is stopping...")
        output = subprocess.run(["sc", "query", service], capture_output=True, text = True)
        status = output.stdout.strip()
        if "RUNNING" in status:
            print("service failed to stop")
        print("if you wanted the service to start use start in menu options \n (restart return's service to state that it was before restart)")


print("if you wanted the service to start use start in menu options \n (restart return's service to state that it was before restart)")
