# Remove an item only if it is present in the set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Check if 2 is present and remove it
if 2 in my_set:
    my_set.remove(2)
    print("After removing 2:", my_set)
else:
    print("Item 2 not found in the set.")
