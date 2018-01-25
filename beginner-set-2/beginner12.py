num =int(input("Number: "))
str1=""
while num>0:
    str1= str1+(str(num%10))
    num//=10
revstr="".join(reversed(str1))
if str1==revstr:
    print("Yes")
else:
    print("No")