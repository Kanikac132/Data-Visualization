# program to check if string is palindrome
# Taking input from user
s = input("Enter string: ")

rev = ""
for ch in s:
    rev = ch + rev

if s == rev:
    print("Yes")
else:
    print("No")