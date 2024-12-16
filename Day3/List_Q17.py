# Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

Sample_list  = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
unique = []
for i in Sample_list:
  if i not in unique:
    unique.append(i)
sorted(unique)