#  program to remove spaces from string
# Taking input from user
s = input("Enter string: ")

result = ""
for ch in s:
    if ch != " ":
        result += ch

print(result)