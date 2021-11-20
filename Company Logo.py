
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    l=[]
    l1=[]
    for i in s:
        c=0
        for j in s:
            if(j==i):
                c+=1
        if i not in l:
            l.append(i)
            l1.append(c)
    for i in range(0,len(l1)):
        for j in range(0,len(l1)-1):
            if(l1[j]<l1[j+1]):
                t=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=t
           
                t1=l[j]
                l[j]=l[j+1]
                l[j+1]=t1
    for i in range(0,3):
        if l1[0]==l1[1]==l1[2]:
            l.sort()
        else:
            if l1[i]==l1[i+1]:
                if l[i]>l[i+1]:
                    t=l[i]
                    l[i]=l[i+1]
                    l[i+1]=t
        print(l[i],l1[i])
