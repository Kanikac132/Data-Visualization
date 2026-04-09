#  function to calculate total bill amount
# A billing system calculates totals
def total_bill(lst):
    total = 0
    for i in lst:
        total += i
    return total

nums = list(map(int, input("Enter values: ").split()))
print(total_bill(nums))