# Write a Python script to sort (ascending and descending) a dictionary by value.
def sort_dict(mydict):
  print("Ascending Order")
  for key, value in sorted(mydict.items(), key = lambda x: x[1]):
    print(key, "--->", value)

  print("Descending Order")
  for key, value in sorted(mydict.items(), key = lambda x: x[1], reverse = True):
    print(key, "--->", value)

sort_dict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})