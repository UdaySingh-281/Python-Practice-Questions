# Write a Python program to remove duplicates from a list.

my_list = [1, 2, 3, 4, 5, 2, 3, 4, 2, 2]

for i in my_list:
  while my_list.count(i) != 1:
    print("Removing ",i)
    my_list.remove(i)
my_list