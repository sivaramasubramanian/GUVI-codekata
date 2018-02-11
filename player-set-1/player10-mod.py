word1=input()
word2=input()
count=0


for i ,j in zip(word1,word2):
        if i!=j:
            count+=1

if count==1:
    print("Yes")
else:
    print("No")

