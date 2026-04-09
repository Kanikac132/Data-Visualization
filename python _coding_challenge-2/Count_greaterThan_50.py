#  program to count numbers greater than 50 in a list
# Taking input from user
nums = list(map(int, input("Enter numbers: ").split()))

count = 0
for i in nums:
    if i > 50:
        count += 1

print("Count =", count)