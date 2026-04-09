#  program to rotate list by one position
# Taking input from user
lst = list(map(int, input("Enter list: ").split()))

last = lst[-1]
for i in range(len(lst)-1, 0, -1):
    lst[i] = lst[i-1]

lst[0] = last

print(lst)