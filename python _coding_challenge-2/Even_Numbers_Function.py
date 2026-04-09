#  function to return all even numbers from lis
# A report filters values
def even_numbers(lst):
    res = []
    for i in lst:
        if i % 2 == 0:
            res.append(i)
    return res

nums = list(map(int, input("Enter list: ").split()))
print(even_numbers(nums))