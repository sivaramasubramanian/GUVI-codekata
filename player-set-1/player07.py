word=input()
ar=[x for x in word]

for i in range(0,len(word)-1,2):
    c=ar[i+1]
    ar[i+1]=ar[i]
    ar[i]=c

print(ar)