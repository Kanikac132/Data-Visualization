# Taking input from user
salary = int(input("Enter salary: "))

bonus = 0
if salary > 0:
    bonus = salary * 7 / 100

print("Bonus =", int(bonus))