num=int(input())
sum_of_squares=0
while num >0:
    last_digit=(num%10)
    sum_of_squares+=(last_digit**2)
    num//=10
print(sum_of_squares)