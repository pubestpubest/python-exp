# Classes and Objects in Python

# Defining a class
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating objects
mikey = Dog("Mikey", 6)
lucy = Dog("Lucy", 3)

# Accessing class attributes
print(mikey.species)
print(lucy.species)

# Accessing instance attributes
print(mikey.name)
print(mikey.age)

# Calling instance methods
print(mikey.description())
print(mikey.speak("Woof Woof"))
print(lucy.description())
print(lucy.speak("Bark"))

# Defining another class
class Car:
    # Initializer / Instance attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Instance method
    def description(self):
        return f"{self.year} {self.make} {self.model}"

# Creating objects
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2018)

# Accessing instance attributes
print(car1.make)
print(car1.model)
print(car1.year)

# Calling instance methods
print(car1.description())
print(car2.description())
