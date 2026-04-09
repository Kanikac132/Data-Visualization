# program to count number of digits
# Taking input from user
num = int(input("Enter number: "))

count = 0
while num > 0:
    count += 1
    num = num // 10

print("Digits =", count)