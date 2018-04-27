print("Welcome to the shopping website!")
print("Please login to the website first:")

import re,shoplistmodule,sys
address=sys.path[0]+"/shopping_customer"
def login():
    username=input("Username:")
    password=input("Password:")
    status=False

    f=open(address,mode="r")
    for line in f:
        unumber,uname,upass=line.split()

        if username==uname and password==upass:
            status=True
            break

    if status==True:
        print("Login successfully!")
        shoplistmodule.shoplist()

    else:
        print("Login Failed. Please Try again")
        login()

login()