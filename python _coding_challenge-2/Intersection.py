#  program to find intersection
# Taking input from user
a = set(map(int, input("Enter set1: ").split()))
b = set(map(int, input("Enter set2: ").split()))

inter = set()
for i in a:
    if i in b:
        inter.add(i)

print(inter)
