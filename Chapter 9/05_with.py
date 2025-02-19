# f = open("file.txt")
# print(f.read())
# f.close()

# Same can be done using with statement

with open("file.txt") as f:
    print(f.read())

# The with statement automatically closes the file when the block is exited.
# The with statement is a good practice to use when working with file objects.