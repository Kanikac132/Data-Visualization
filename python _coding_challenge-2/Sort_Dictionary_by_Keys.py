#  program to sort dictionary by keys.
# A dictionary needs sorting
d = {"b":2, "a":1}

keys = list(d.keys())
keys.sort()

sorted_dict = {}
for k in keys:
    sorted_dict[k] = d[k]

print(sorted_dict)