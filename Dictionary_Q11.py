# Write a Python program to convert a list into a nested dictionary of keys.

nested_dict = {}
mylist = [1,2,3,4]

for i in mylist:
  nested_dict[i] = {}
  i = nested_dict[i]
print(nested_dict)