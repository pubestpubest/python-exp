# File I/O in Python

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a file I/O example.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a file
with open("example.txt", "a") as file:
    file.write("Appending a new line to the file.\n")

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
