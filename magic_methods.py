# Magic Methods in Python

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
