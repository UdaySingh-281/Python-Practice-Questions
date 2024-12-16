# Sorting a list of tuples by the last element in each tuple
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_list = sorted(sample_list, key=lambda x: x[-1])

print("Sorted list by the last element of each tuple:", sorted_list)