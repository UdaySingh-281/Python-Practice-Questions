# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

mystr = list(input("Enter the string: "))
mydict= dict()
for i in mystr:
  x = mystr.count(i)
  mydict[i] = x
print(mydict)