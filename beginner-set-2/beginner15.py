start =int(input())
end = int(input())
if start%2==0:
    start+=2
else:
    start+=1

for i in range(start,end,2):
    print(i)
