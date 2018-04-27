import sys,os,json
sys.path.append(os.path.dirname(sys.path[0]))
from db import Accounts
from Core import logger

def creditpay(total):
    cardno = input("Card Number:")
    cardpa = input("Password:")
    if os.path.exists(os.path.dirname(sys.path[0])+'/db/Accounts/%s.json'%cardno):
        abspath=os.path.dirname(sys.path[0]) + '/db/Accounts/%s.json' % cardno
        f=open(abspath,mode='r')
        data=json.load(f)
        rpass=data.get("password")
        if rpass==cardpa:
            print("Successfully login!")
            acredit=data.get("credit")
            balance=data.get("balance")
            update_acredit=acredit-total
            if update_acredit<0:
                print("Your available credit is %s and the transaction needs %s. We cannot proceed this transaction."%(acredit,total))
            else:
                data["credit"]=update_acredit
                print("Credit card pays this bill successfully")
                os.chdir(os.path.dirname(sys.path[0])+'/db/Accounts')
                t=open("%s.1.json"%cardno,mode="w+")
                json.dump(data,t)
                t.close()
                os.remove("%s.json"%cardno)
                os.renames("%s.1.json"%cardno,"%s.json"%cardno)
                print('''
--------Your Current Balance-------
Current Credit:%s
Current Balance:%s
-------Thank you for shopping------'''%(update_acredit,balance))
                log_type=logger.logger("transactions")
                log_type.info("account:%s   action:ShoppingMall    amount:%s   interest:0" % (cardno, total))
        else:
            print("Incorrect password!")

    else:
        print("Account does not exist. Please try again")
        creditpay(total)