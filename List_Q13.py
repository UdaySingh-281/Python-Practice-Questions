# Function to append a list to another list
def append_list(list1, list2):
    list1.extend(list2)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

append_list(list1, list2)

print("Modified list1 after appending list2:", list1)
