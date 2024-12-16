# Write a Python program to get the last part of a string before a specified character.

mystr = input("Enter the String: ")
mychar = input("Enter the Character: ")

print(mystr.rsplit(mychar,1)[0])