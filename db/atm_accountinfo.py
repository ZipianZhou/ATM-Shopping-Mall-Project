import json
import sys,os
sys.path.append(os.path.dirname(sys.path[0]))
import bin
from bin import 管理员2


account = {"number": "0001", "pass": "0002", }


acc_dic = {
    1234:{
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0
     # 0 = normal, 1 = locked, 2 = disabled
    },
    2345: {
        'password': 'abc',
        'credit': 15000,
        'balance': 15000,
        'enroll_date': '2016-01-02',
        'expire_date': '2021-01-01',
        'pay_day': 22,
        'status': 0
        # 0 = normal, 1 = locked, 2 = disabled
    }
}
def change_status(cardno):
    cardno=int(cardno)

    change=input("change status to:")
    acc_dic[cardno]["status"]=change
    for i in acc_dic:
        f = open("%s.json" % (i), mode="w")
        json.dump(acc_dic.get(i), f)
#
def change_credit(cardno):
    cardno = int(cardno)
    change = input("change credit to:")
    acc_dic[cardno]["credit"] = change
    for i in acc_dic:
        f = open("%s.json" % (i), mode="w")
        json.dump(acc_dic.get(i), f)

def add():
    print("Link to add!")
    cardno=input("Input the new account number:")
    if os.path.exists(updatepath+"/Accounts/%s.json"%cardno):
        print("This account already exist")
    else:
        add_account(cardno)

def editlimit():
    print("Link to edit limit!")
    while True:
        cardno=input("Cardno that need to change status:")
        if os.path.exists(updatepath+"/Accounts/%s.json"%cardno):
            change_credit(cardno)
            print("Successfully changed account %s's credit."%(cardno))
            return
        else:
            print("Cardno does not exist.")
            break

def disable():
    print("Link to disable!")
    while True:
        cardno=input("Cardno that need to change status:")
        if os.path.exists(updatepath+"/Accounts/%s.json"%cardno):
            change_status(cardno)
            print("Successfully changed account %s's status."%(cardno))
            return
        else:
            print("Cardno does not exist.")
            #disable()
            break


def add_account(cardno):
    value=cardno
    cardno={}
    password=input("password:")
    credit=input("credit:")
    balance = input("balance:")
    enroll = input("enroll_date:")
    expire = input("expire_date:")
    payday = input("pay day:")
    state = input("status:")
    cardno["password"]=password
    cardno["credit"]=credit
    cardno["balance"] = balance
    cardno["enroll_date"] = enroll
    cardno["expire_date"] = expire
    cardno["pay_day"] = payday
    cardno["status"] = state
    os.chdir(updatepath + "/Accounts")
    f=open("%s.json"%value,mode="w")
    json.dump(cardno,f)
    print("successfully add an account!")

def handler(value):
    menu.get(value)()
    return 管理员2.Manage()


absdb=os.path.abspath("db")
updatepath=os.path.dirname(os.path.dirname(absdb))+"/db"

os.chdir(updatepath+"/Accounts")


menu={
    "1":add,
    "2":editlimit,
    "3":disable
}
