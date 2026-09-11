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

activateProcess()
