# Create a module with a function to add two numbers and import it
# A module performs calculations
# file1.py
def add(a, b):
    return a + b

# file2.py
from file1 import add

print(add(2,3))