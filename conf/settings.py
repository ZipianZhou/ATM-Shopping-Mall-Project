import os
import sys
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)


DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name':'accounts',
    'path': "%s/db" % BASE_DIR
}


LOG_LEVEL = logging.INFO

LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}

TRANSACTION_TYPE = {
    'Repay':{'action':'plus', 'interest':0},
    'Withdraw':{'action':'minus', 'interest':0.05},
    'Transfer':{'action':'minus', 'interest':0.05},
    'Buy':{'action':'minus', 'interest':0},
}