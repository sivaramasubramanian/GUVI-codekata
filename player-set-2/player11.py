day=input().title()
days_rem=("Monday","Tuesday","Wednesday","Thursday","Friday")
if day=='Sunday' or day=='Saturday':
    print("yes")
elif day in days_rem:
    print("no")
else:
    print("Invalid")