#  program to check if a number is positive, negative, or zero
# Taking input from user
num = int(input("Enter number: "))

if num == 0:
    print("Zero")
else:
    if num > 0:
        print("Positive")
    else:
        print("Negative")