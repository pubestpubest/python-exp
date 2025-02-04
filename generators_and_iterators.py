# Generators and Iterators in Python

# Generator function
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Using the generator function
counter = count_up_to(5)
for num in counter:
    print(num)

# Generator expression
squares = (x * x for x in range(10))
for square in squares:
    print(square)

# Custom iterator class
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current

# Using the custom iterator class
my_range = MyRange(1, 5)
for num in my_range:
    print(num)
