# program to find union of two sets
# Taking input from user
a = set(map(int, input("Enter set1: ").split()))
b = set(map(int, input("Enter set2: ").split()))

union = a.copy()
for i in b:
    union.add(i)

print(union)