#finding repeated items in a tuple

my_tuple = (1, 2, 3, 2, 4, 1, 5, 3)
repeated_items = []
for i in my_tuple:
  if my_tuple.count(i) > 1 and i not in repeated_items:
    repeated_items.append(i)
print(repeated_items)