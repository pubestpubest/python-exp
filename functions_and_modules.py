# Functions and Modules in Python

# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling a function
print(greet("Alice"))

# Importing a module
import math

# Using a function from the imported module
print(math.sqrt(16))

# Importing a specific function from a module
from math import pi

# Using the imported function
print(pi)

# Creating a custom module
# Save this code in a file named `my_module.py`
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Importing the custom module
import my_module

# Using functions from the custom module
print(my_module.add(5, 3))
print(my_module.subtract(5, 3))
