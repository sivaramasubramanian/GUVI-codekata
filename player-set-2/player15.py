try:
    word1=input().lower()
    arr={}

    for ch in word1:
        if ch in arr:
            arr[ch]+=1
        else:
            arr[ch]=1

    max=-1
    char=''

    for letter,count in zip(arr.keys(),arr.values()):
        if count > max:
            max = count
            char=letter

    print(char)
except:
    print('invalid')
