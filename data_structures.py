# Data Structures in Python

# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("orange")
print(fruits)
print(fruits[1])
print(len(fruits))  # Built-in function: list length
fruits.sort()  # Built-in function: list sort
print(fruits)

# Tuples
vegetables = ("carrot", "broccoli", "spinach")
print(vegetables)
print(vegetables[0])

# Dictionaries
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)
print(person["name"])
person["email"] = "alice@example.com"
print(person)
print(len(person))  # Built-in function: dictionary length
print(person.keys())  # Built-in function: dictionary keys
print(person.values())  # Built-in function: dictionary values

# Sets
numbers = {1, 2, 3, 4, 5}
print(numbers)
numbers.add(6)
print(numbers)
print(3 in numbers)
print(len(numbers))  # Built-in function: set length
numbers.remove(2)  # Built-in function: set remove
print(numbers)
