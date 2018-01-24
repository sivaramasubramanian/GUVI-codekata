#maximun of three numbers
a=int(input("First Number"))
b=int(input("Second Number"))
c=int(input("Third Number"))

if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)