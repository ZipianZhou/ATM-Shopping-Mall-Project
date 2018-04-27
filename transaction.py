import sys,os,json,pickle,time
from Core import main,logger

from conf import settings

def trans(cardno,log_obj,logintime):
    while True:
        print("------List of command------")
        time.time()
        if time.time()-logintime>=360:
            print("Sorry,your session has expired")
            log_obj.info("%s This account has logged out."%cardno)
            log_obj.handlers.pop()
            exit()

        for i in settings.TRANSACTION_TYPE:
            print(i)

        command = input("command:")
        if command == "Exit":
            print("Successfully logout!")
            print("Log out time is " + time.asctime())
            log_obj=logger.logger("access")
            log_obj.info("%s This account has logged out." % cardno)
            log_obj.handlers.pop()
            exit()
        else:
            amount = input ('amount:')
            if amount.isdigit():
                amount=int(amount)
            else:
                print("Invalid amount.Please try again.")
                trans(cardno,log_obj,logintime)
        break


    if command in settings.TRANSACTION_TYPE:

        from db import Accounts
        os.chdir(os.path.dirname(sys.path[0])+'/db/Accounts')
        f= open("%s.json"%(cardno),mode="r")
        data=json.load(f)
        oldbalance=data.get("balance")

        interest=amount*settings.TRANSACTION_TYPE[command].get("interest")
        if settings.TRANSACTION_TYPE[command].get("action")=="plus":
            current_balance=oldbalance + amount + interest
            change=current_balance-oldbalance
        elif settings.TRANSACTION_TYPE[command].get("action") == "minus":
            current_balance = oldbalance - amount - interest
            change=amount
            if current_balance<0:
                print("Your credit %s is not enough for this transaction %s. Your current balance is %s. Please enter again."%(data.get("credit"),amount,oldbalance))
                return trans(cardno)
        data["balance"]=current_balance

        f=open("%s.1.json"%cardno,mode='w+')
        json.dump(data,f)
        f.close()
        os.remove("%s.json"%cardno)
        os.renames("%s.1.json"%cardno,"%s.json"%cardno)
        log_obj=logger.logger("transactions")
        # print(log_obj)
        if command == "Repay":
            log_obj.info("account:%s   action:%s    amount:%s   interest:%s" % (cardno, command, amount,interest))
            main.Repay(command,cardno,amount,current_balance,change)
            log_obj.handlers.pop()
        elif command == "Withdraw":
            log_obj.info("account:%s   action:%s    amount:%s   interest:%s" % (cardno, command, amount, interest))
            main.Withdraw(command,cardno,amount,current_balance,change)

            log_obj.handlers.pop()
        elif command == "Buy":
            log_obj.info("account:%s   action:%s    amount:%s   interest:%s" % (cardno, command, amount, interest))
            main.Buy(command,cardno,amount,current_balance,change)

            log_obj.handlers.pop()
        elif command == "Transfer":
            log_obj.info("account:%s   action:%s    amount:%s   interest:%s" % (cardno, command, amount, interest))
            main.Transfer(command,cardno,amount,current_balance,change)

            log_obj.handlers.pop()
        trans(cardno,log_obj,logintime)


    else:
        print("Invalid command.Please try again.")
        trans(cardno,log_obj,logintime)
