roman=input().upper()
roman_value={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
int_value=0
for i in range (len(roman)):
    if i>0 and roman_value[roman[i]]>roman_value[roman[i-1]]:
      int_value+=roman_value[roman[i]]-2*roman_value[roman[i-1]]
    else:
      int_value+=roman_value[roman[i]]
print(int_value)
