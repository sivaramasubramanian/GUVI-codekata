#Armstrong Number
import math
n =int(input())

def isArmstrong(n):
    num=n
    res=0
    while num>0:
        res+=((num%10)**3)
        num//=10
    if res==n:
        return True
    else:
        return False

if isArmstrong(n):
    print("Yes")
else:
    print("No")

