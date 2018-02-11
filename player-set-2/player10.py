word1=input()
word2=input()
dict={}
alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in alphabet:
    dict[char]=0

for ch in word1:
    dict[ch]+=1

for ch in word2:
    dict[ch]-=1

flag=False
sum=0

for char in dict:
    count=dict[char]
    sum+=count
    if count == 1:
        flag=True
    if flag and count>1:
        flag=False
        break

if flag and sum==0:
    print("Yes")
else:
    print("No")
