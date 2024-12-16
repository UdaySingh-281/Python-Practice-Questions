# Function to find common items from two lists
def find_common_items(list1, list2):
    common_items = set(list1) & set(list2)
    return list(common_items)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_items = find_common_items(list1, list2)

print("Common items:", common_items)
