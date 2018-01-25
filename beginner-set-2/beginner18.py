import math
start =int(input())
end =int(input())

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

for i in range(start,end):
    if isArmstrong(i):
        print(i)
