#  program to classify the user as Minor, Adult, or Senior.
# Taking input from user
age = int(input("Enter age: "))

if age >= 18:
    if age >= 60:
        print("Senior")
    else:
        print("Adult")
else:
    print("Minor")