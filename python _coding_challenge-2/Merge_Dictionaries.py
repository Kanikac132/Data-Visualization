# program to merge dictionaries
# A system merges two dictionaries.
d1 = {"a":1}
d2 = {"b":2}

for key in d2:
    d1[key] = d2[key]

print(d1)