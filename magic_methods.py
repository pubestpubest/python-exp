# Magic Methods in Python

# Magic methods, also known as dunder methods (short for "double underscore"), are special methods in Python that start and end with double underscores. They allow you to define the behavior of your objects for built-in operations such as addition, subtraction, string representation, and more. By implementing magic methods, you can make your custom classes behave like built-in types.

# Defining a class with magic methods
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented

# Creating objects
book1 = Book("1984", "George Orwell", 328)
book2 = Book("Animal Farm", "George Orwell", 112)

# Using magic methods
print(str(book1))
print(repr(book1))
print(len(book1))
print(book1 == book2)
print(book1 + book2)

# Explanation of magic methods

# __init__: This method is called when an instance of the class is created. It initializes the object's attributes.
# __str__: This method is called by the str() function and the print statement to get a string representation of the object.
# __repr__: This method is called by the repr() function and is used to get a string representation of the object that can be used to recreate the object.
# __len__: This method is called by the len() function to get the length of the object.
# __eq__: This method is called by the == operator to compare two objects for equality.
# __add__: This method is called by the + operator to add two objects together.
