ch =input().lower()[0]
vowels = "aeiou"
if ch in vowels[:]:
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not a Alphabet")