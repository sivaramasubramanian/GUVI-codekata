n=int(input())
k=int(input())
sum=0
for i in range(n):
    x=int(input())
    if i<k:
        sum+=x
print(sum)