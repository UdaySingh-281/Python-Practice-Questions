# Write a Python program to count the number of characters (character frequency) in a
# string.
# Sample String : google.com
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

mystr = input("Enter the String: ")
mydict = dict()

for i in mystr:
  if i not in mydict:
    mydict[i] = mystr.count(i)

print(mydict)