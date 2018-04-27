import sys,os
sys.path.append(os.path.dirname(sys.path[0]))
from db import atm_accountinfo

functions = '''1:"Add a new account",
2:"Edit user's card limit",
3:"Disable user's account" '''

def Manage():
    while True:
        print("------Management Page------")
        print(functions)
        choice = input("Number:")
        if choice == "Exit":
            print("Successfully logout!")
            exit()
        else:
            if choice.isdigit():
                if int(choice) <= 3:
                    from db import atm_accountinfo

                    atm_accountinfo.handler(choice)

                else:
                    print("Invalid Input. Please try again.")
                    Manage()

        break