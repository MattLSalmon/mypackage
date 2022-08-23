import sys
import os
sys.path.append(os.path.join(os.path.abspath(__file__), r'../..'))

import module2
from module2 import import_math



def add(a, b):
    return a+b 

if __name__ == "__main__":
    print(add(1,2))    
    print(module2.import_math.subtract(2,3))
    print(import_math.subtract(2, 3))