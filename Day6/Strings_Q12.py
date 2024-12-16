# Write a Python program to lowercase first n characters in a string.

text = input("Enter the string: ")
n = int(input("Enter the number: "))

text = text.replace(text[0:n], text[0:n].upper())
print(text)