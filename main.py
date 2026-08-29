import sysD as d
import runit as r
import os

while True:
    print("="*32)
    print("SimpleServiceScript-SSS-".center(32))
    print("="*32)
    print("What are you using?".center(32))
    print("="*32)
    print(" [1] runit")
    print(" [2] systemD")
    print(" [0] exit")
    print("="*32)

    option = input("choose one of the options above: ")

    if option == "1":
        while True:
            os.system("clear")
            # this took like 5 min to make
            # cause idk how to copy
            # paste on neovim
        
            print("="*32)
            print("runit".center(32))
            print("="*32)
            print("[1] start service".center(32))
            print("[2] stop service".center(32))
            print("[3] restart service".center(32))
            print("[4] service status".center(32))
            print("[0] exit".center(32))
            print("="*32)
            # ts is taking way to long to do
            option = input("choose one of the options above: ")

            if option == "1":
                os.system("clear")
                r.activateProcessR()
            elif option == "2":
                os.system("clear")
                r.deactivateProcessR()
            elif option == "3":
                os.system("clear")
                r.restartProcessR()
            elif option == "4":
                os.system("clear")
                r.processStatusR()
            elif option == "0":
                os.system("clear")
                break
            else:
                os.system("clear")
                print("invalid option")

    elif option == "2":
        while True:
            os.system("clear")

            print("="*32)
            print("SystemD".center(32))
            print("="*32)
            print(" [1] start service")
            print(" [2] stop service")
            print(" [3] restart service")
            print(" [4] service status")
            print(" [0] exit")
            print("="*32)

            option = input("choose one of the options above: ")

            if option == "1":
                os.system("clear")
                d.activateProcess()
            elif option == "2":
                os.system("clear")
                d.deactivateProcess()
            elif option == "3":
                os.system("clear")
                d.restartProcess()
            elif option == "4":
                os.system("clear")
                d.processStatus()
            elif option == "0":
                os.system("clear")
                break
            else:
                os.sytem("clear")
                print("invalid option")
    elif option == "0":
        os.system("clear")
        exit(0)
    else:
        print("invalid option")





