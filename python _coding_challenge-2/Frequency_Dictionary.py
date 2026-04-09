#  program to count frequency of elements using dictionary
# A system groups data. 
lst = list(map(int, input("Enter list: ").split()))

d = {}
for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)