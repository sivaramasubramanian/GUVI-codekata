try:
    word=input()
    vowels=('a','e','i','o','u')
    no_vowels="".join([ch for ch in reversed(word) if ch.lower() not in vowels])
    print(no_vowels)
except:
    print("invalid")