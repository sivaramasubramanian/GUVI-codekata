#count no of digits
n=int(input())
digits=0
while n>0:
    digits+=1
    n//=10
print(digits)