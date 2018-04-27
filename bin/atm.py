import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from Core import atm_auth

if __name__ == '__atm_auth__':
    atm_auth.run()