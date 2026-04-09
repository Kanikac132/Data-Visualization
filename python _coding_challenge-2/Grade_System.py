#  program to assign grade based on marks
# Taking input from user
marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")