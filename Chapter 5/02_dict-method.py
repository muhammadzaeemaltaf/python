d ={} # Empty dictionary

marks = {
    'John': 90,
    'Jane': 85,
    'Jack': 87,
    'Jill': 92
}

# Using keys(), values(), and items() methods
print("Keys:", marks.keys())
print("Values:", marks.values())
print("Items:", marks.items())

# Update dictionary with new values
marks.update({'John': 95, 'Alice': 88})
print("After update:", marks)

# Get a value with get()
print("John's mark:", marks.get('John'))

# Using pop() to remove a key and return its value
removed_mark = marks.pop('Jane', 'Not Found')
print("Removed Jane's mark:", removed_mark)
print("After pop:", marks)

# Using setdefault() to add a key with a default value if it doesn't exist
default_mark = marks.setdefault('Paul', 80)
print("Paul's mark (setdefault):", default_mark)
print("After setdefault:", marks)

# Using popitem() to remove and return the last inserted (key, value) pair
last_item = marks.popitem()
print("Popped item:", last_item)
print("After popitem:", marks)

# Copying the dictionary
marks_copy = marks.copy()
print("Copied dictionary:", marks_copy)