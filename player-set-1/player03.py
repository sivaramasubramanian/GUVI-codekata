num=int(input())
rev_num=0
while num >0:
    rev_num*=10
    rev_num+=(num%10)
    num//=10
print(rev_num)