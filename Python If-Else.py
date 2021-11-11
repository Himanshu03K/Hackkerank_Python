import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2!=0 :
    print("Weird")
else :
    c=0
    x=6
    if n==4 :
        print("Not Weird")
    else :
        for x in range(21):
            if n==x :
                c=1
                break    
        if c==1 :
            print("Weird")
        else :
            print("Not Weird")
    
    
