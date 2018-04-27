import sys,os,json
from Core import logger
sys.path.append(os.path.dirname(sys.path[0]))
from conf import settings


def Repay(command,cardno,amount,current_balance,change):
    f = open("%s.json" % (cardno), mode="r")
    data = json.load(f)
    balance_info = '''------Balance Information------
Current Balance:%s
Current Credit:%s''' % (data.get("balance"), data.get("credit"))

    print (balance_info)


    print("repay successfully!")


def Withdraw(command,cardno,amount,current_balance,change):
    f = open("%s.json" % (cardno), mode="r")
    data = json.load(f)
    balance_info = '''------Balance Information------
Current Balance:%s
Current Credit:%s''' % (data.get("balance"), data.get("credit"))
    print(balance_info)
    print("withdraw successfully!")


def Transfer(command,cardno,amount,current_balance,change):
    import db
    abspath=sys.path[0]
    cardto=input("Transfer to:")
    if os.path.exists(os.path.dirname(abspath) + "/db/Accounts" + "/%s.json" % (cardto)):
        t=open("%s.json" % (cardto), mode="r")
        data1=json.load(t)
        taccount=data1.get("balance")
        taccount=taccount+change
        data1['balance']=taccount
        t = open("%s.1.json" % (cardto), mode="w+")
        json.dump(data1,t)
        os.remove("%s.json" % (cardto))
        os.renames("%s.1.json" % (cardto),"%s.json" % (cardto))
        f = open("%s.json" % (cardno), mode="r")
        data = json.load(f)
        balance_info = '''------Balance Information------
Current Balance:%s
Current Credit:%s''' % (data.get("balance"), data.get("credit"))
        print(balance_info)
        print("transfer successfully!")
    else:
        print("Invalid transfer account. Please try again")




def Buy(command,cardno,amount,current_balance,change):
    f = open("%s.json" % (cardno), mode="r")
    data = json.load(f)
    balance_info = '''------Balance Information------
Current Balance:%s
Current Credit:%s''' % (data.get("balance"), data.get("credit"))
    print(balance_info)
    print("buy successfully!")
