# 添加账户、用户额度，冻结账户
import sys,os
sys.path.append(os.path.dirname(sys.path[0]))
import db,管理员2
account={"number":"0001","pass":"0002",}

def login(func):
    def inner():
        maaccount = input("Management account number:")
        mapass = input("Management account password:")
    return inner


@login
def manage(maaccount,mapass):
    if maaccount == account.get("number") and mapass == account.get("pass"):
        return 管理员2.Manage()
    else:
        print("Invalid account number or password. Please try again.")
        return manage()

manage()