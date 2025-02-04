# Inheritance and Polymorphism in Python

# Defining a base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Defining a derived class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Demonstrating polymorphism
def animal_sound(animal):
    print(animal.speak())

# Creating objects of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the polymorphic function
animal_sound(dog)
animal_sound(cat)
