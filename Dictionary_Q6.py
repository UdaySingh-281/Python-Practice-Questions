# Write a Python program to remove a key from a dictionary.
mydict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
x = int(input("Enter the key to be deleted: "))
if x in mydict:
  mydict.pop(x)
  print(mydict)
  print("Item removed")
else:
  print("Item Not present")