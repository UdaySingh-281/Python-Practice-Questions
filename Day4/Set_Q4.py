# Removing an element from the set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Removing a single element
my_set.remove(3)
print("After removing 3:", my_set)

# Removing an element using discard (no error if item is not found)
my_set.discard(4)
print("After discarding 4:", my_set)
