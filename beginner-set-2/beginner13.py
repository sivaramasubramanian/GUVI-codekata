import math
num =int(input("Number: "))
isPrime=True
for i in range(2,int(math.sqrt(num)+1)):
    if num%i==0:
        isPrime=False
        break
if isPrime and num>=2:
    print("yes")
else:
    print("no")
