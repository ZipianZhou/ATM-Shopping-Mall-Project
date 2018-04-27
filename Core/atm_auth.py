import sys,os,json,time
from Core import transaction
# from Core import account,logger
from Core import logger
print("Welcome to ATM service!")

def atm_auth(func):
    def inner(*args,**kwargs):
        cardno=input("Card Number:")
        cardpa=input("Password:")
        log_obj=logger.logger("access")
        return func(cardno,cardpa,log_obj)
    return inner

abspath=os.path.abspath("account")


@atm_auth
def find_account(cardno,cardpa,log_obj):

    if os.path.exists(os.path.dirname(os.path.dirname(abspath))+"/db/Accounts"+"/%s.json"%(cardno)):
        accountpath=os.path.dirname(os.path.dirname(abspath))+"/db/Accounts"+"/%s.json"%(cardno)
        f=open(accountpath,mode="r")
        info=json.load(f)
        if cardpa==info.get("password"):
            if info.get("status")==0:
                print("Login Successfully!")
                log_obj.info("%s This account has logged in."%cardno)
                log_obj.handlers.pop()
                t=time.localtime()
                time.mktime(t)
                print("Log in time is " + time.asctime())
                logintime=time.time()

                transaction.trans(cardno,log_obj,logintime)

            else:
                print("Sorry,your account has been locked. Please contact the officer to verify your identity.")
        else:
            print("Invalid Password. Please try again")

            find_account2(cardno,log_obj)
    else:
        print("Card Number does not exist")
        import atm_auth
        atm_auth.atm_auth()

def find_account2(cardno,log_obj):
    accountpath = os.path.dirname(os.path.dirname(abspath)) + "/db/Accounts" + "/%s.json" % (cardno)
    f = open(accountpath, mode="r")
    info = json.load(f)
    retry=0
    while True:
        print("cardno:%s"%cardno)
        cardpa=input("password:")
        if cardpa == info.get("password"):
            print("Login Successfully!")
            logintime = time.time()
            transaction.trans(cardno,log_obj,logintime)
            break
        else:
            retry+=1
            if retry<3:
                pass
            else:
                print("Your account has been locked.")
                change_status_direct=os.path.dirname(sys.path[0])+"/db"
                sys.path.append(change_status_direct)
                os.chdir(change_status_direct)
                import atm_accountinfo
                atm_accountinfo.change_status(cardno)
                log_obj.error("%s This account has failed login for more than three times."%cardno)
                log_obj.handlers.pop()


                break

find_account()

