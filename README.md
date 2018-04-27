# ATM-Shopping-Mall-Project
This is an ATM + Shopping Mall Project using python3 to finish.
ATM + 购物车程序/

├── README

├── atm #ATM主程目录

│   ├── __init__.py

│   ├── bin #ATM 执行文件 目录

│   │   ├── __init__.py

│   │   ├── atm.py  #ATM 执行程序

│   │   ├── 管理员.py #ATM 管理端

│   │   └── 管理员2.py #ATM 管理端被调用程序

│   ├── conf #配置文件

│   │   ├── __init__.py

│   │   └── settings.py

│   ├── core #主要程序逻辑都 在这个目录 里

│   │   ├── __init__.py

│   │   ├── atm_auth.py      #用户认证模块,从文件里加载和存储账户数据

│   │   ├── logger.py       #日志记录模块

│   │   ├── main.py         #主逻辑交互程序

│   │   └── transaction.py  #记账\还钱\取钱等所有的与账户金额相关的操作,以及定时结束当前进程，让用户退出

│   ├── db  #用户数据存储的地方

│   │   ├── Accounts文件夹，下面储存用户json文件

│   │       └── 1234.json #用户账户示例文件

│   │   ├── __init__.py

│   │   ├── atm_accountinfo.py #生成一个初始的账户数据 ,把这个数据 存成一个 以这个账户id为文件名的文件,放在accounts目录 就行了,程序自己去会这里找

│   └── log #日志目录

│       ├── __init__.py

│       ├── access.log #用户访问和操作的相关日志

│       └── transactions.log    #所有的交易日志

└── Shopping #电子商城程序

│       └── __init__.py

│       ├── creditpay.py     # 信用卡付款接口，

│       ├──shoplistmodule.py  #添加商品，计算金额

│       ├── shoppingcart.py     #购物车程序认证入口

 

│       └──shopping_customer.txt    #购物商城用户信息
