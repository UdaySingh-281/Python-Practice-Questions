# Function to check if two lists have at least one common member
def have_common_member(list1, list2):
    return bool(set(list1) & set(list2))

list1 = ['Red', 'Green', 'Blue']
list2 = ['Yellow', 'Green', 'Pink']

result = have_common_member(list1, list2)
print("Do the lists have a common member?", result)