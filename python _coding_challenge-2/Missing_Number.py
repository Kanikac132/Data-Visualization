# program to find missing number
# Taking input from user
lst = list(map(int, input("Enter numbers: ").split()))

n = len(lst) + 1
total = n * (n + 1) // 2

print("Missing =", total - sum(lst))