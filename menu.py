import main as d
import runit as r

while True:
    print("="*32)
    print("SimpleServiceScript-SSS-".center(32))
    print("="*32)
    print("What are you using?".center(32))
    print("="*32)
    print(" [1] runit".center(32))
    print(" [2] systemD".center(32))
    print(" [0] exit".center(32))
    print("="*32)

    option = input("choose one of the options above: ")

    if option == "1":
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
        print("[5] exit".center(32))
        print("="*32)

        option = input("choose one of the options above: ")

        if option == "1":
            activateProcessR()
        elif option == "2":
            deactivateProcessR()
        elif option == "3":
            restartProcessR()
        elif option == "4":
            processStatusR()


