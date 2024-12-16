mylist = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

lst = []
for tuples in mylist:
  lst.append(sorted(tuples))
print(lst)