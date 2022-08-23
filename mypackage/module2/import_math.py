import sys
import os
sys.path.append(os.path.join(os.path.abspath(__file__), r'../..'))

import module1
from module1 import calculation

def subtract(c,d):
    return c-d
    
if __name__ == "__main__":
    print(module1.calculation.add(2,3))
    print(calculation.add(2, 3))