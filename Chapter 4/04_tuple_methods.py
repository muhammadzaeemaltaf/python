a = (1, 2, 3, 4, 3)

# Existing tuple methods
print("Index of 4:", a.index(4))
print("Count of 3:", a.count(3))

# Additional tuple operations:

# 1. Length of the tuple
print("Length of tuple:", len(a))

# 2. Maximum and minimum values
print("Maximum value in tuple:", max(a))
print("Minimum value in tuple:", min(a))

# 3. Slicing the tuple (e.g., first three elements)
print("First three elements:", a[:3])

# 4. Concatenation with another tuple
b = (5, 6)
c = a + b
print("Concatenated tuple:", c)

# 5. Membership check (is an element in the tuple?)
print("Is 2 in tuple?", 2 in a)