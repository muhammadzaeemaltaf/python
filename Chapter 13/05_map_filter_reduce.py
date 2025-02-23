# Map Example

# l = [2, 3, 4, 5, 6]

# square = lambda x: x * x

# sqList = map(square, l) 

# print(list(sqList))


# Filter Example

# def even(n):
#     if n%2 == 0:
#         return True
#     return False

# print(list(filter(even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


# Reduce Example

from functools import reduce

# add = lambda x, y: x + y

# print(reduce(add, [1, 2, 3, 4, 5]))

mul = lambda x, y: x * y

print(reduce(mul, [1, 2, 3, 4, 5]))