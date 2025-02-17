s = {1, 3, 4, 5, 5, 6}
s.add(1)
s.add(2)
s.add(3)

# Let's define two additional sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: all unique elements from both sets
union_set = set_a.union(set_b)
print("Union:", union_set)

# Intersection: elements common to both sets
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)

# Difference: elements in set_a but not in set_b
difference_set = set_a.difference(set_b)
print("Difference (set_a - set_b):", difference_set)

# Symmetric Difference: elements in either set_a or set_b, but not in both
symmetric_diff = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", symmetric_diff)
