# Getting Started with Python

# Variables
x = 5
y = "Hello, World!"

# Data Types
integer_var = 10
float_var = 20.5
string_var = "Python"
list_var = [1, 2, 3, 4, 5]
tuple_var = (1, 2, 3, 4, 5)
dict_var = {"name": "John", "age": 30}
set_var = {1, 2, 3, 4, 5}

# Control Structures
# If statement
if x > 0:
    print("x is positive")

# For loop
for i in list_var:
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Try-Except block
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
