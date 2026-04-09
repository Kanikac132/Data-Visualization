# program to calculate total weekly sales
# Taking input from user
sales = list(map(int, input("Enter 7 days sales: ").split()))

total = 0
for i in sales:
    total = total + i

print("Total Sales =", total)