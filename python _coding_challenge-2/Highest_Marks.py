# program to find student with highest marks from dictionary
# Example dictionary
d = {"A":80, "B":95, "C":78}

max_key = ""
max_val = 0

for key in d:
    if d[key] > max_val:
        max_val = d[key]
        max_key = key

print(max_key)