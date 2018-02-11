def primes_sieve(start,limit):
    a = [True] * limit
    a[0] = a[1] = False
    count=0

    for (i, isprime) in enumerate(a):
        if isprime:
            for n in range(i*i, limit, i):
                a[n] = False
            if start<=i:
                count+=1
              #  print(count," - ",i)
    return count

start=int(input("Enter the starting value: "))
end=int(input("Enter the ending value: "))
noOfPrimes=primes_sieve(start,end)
print(noOfPrimes)