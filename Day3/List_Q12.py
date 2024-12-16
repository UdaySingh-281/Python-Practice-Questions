# Write a Python program to get the difference between the two lists.

def list_difference(list1, list2, items = []):
    for item in list1:
      if item not in list2:
        items.append(item)

    for item in list2:
      if item not in list1:
        items.append(item)
    return items

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

difference = list_difference(list1, list2)

print("Difference between the two lists:", difference)
