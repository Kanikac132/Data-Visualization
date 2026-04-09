#  program to count vowels in a string
# Taking input from user
text = input("Enter string: ")

count = 0
for ch in text:
    if ch.lower() in ['a','e','i','o','u']:
        count += 1

print("Vowels =", count)