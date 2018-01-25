start =int(input())
end = int(input())
if start%2==0:
    start+=1
else:
    start+=2

for i in range(start,end,2):
    print(i)
