# program to find sum of digits
# Taking input from user
num = int(input("Enter number: "))

sum = 0
while num > 0:
    sum += num % 10
    num = num // 10

print("Sum of digits =", sum)