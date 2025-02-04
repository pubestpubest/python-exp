# Context Managers in Python

# Using a context manager with the 'with' statement
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")

# Custom context manager using a class
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

with MyContextManager():
    print("Inside the context")

# Custom context manager using a generator and the contextlib module
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering the context")
    yield
    print("Exiting the context")

with my_context_manager():
    print("Inside the context")
