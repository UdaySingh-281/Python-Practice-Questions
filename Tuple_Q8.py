# Removing an item from a tuple
my_tuple = (10, 20, 30, 40, 50)

my_list = list(my_tuple)

my_list.remove(30)

my_tuple = tuple(my_list)

print("Tuple after removing an item:", my_tuple)
