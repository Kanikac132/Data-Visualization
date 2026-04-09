# program to find the largest among three numbers
# Taking input from user
a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c

print("Largest =", largest)