# Write a Python program to count occurrences of a substring in a string.

text = input("Enter the String: ")
substr = input("Enter the sub-string: ")
count = 0
for i in range(len(text)):
    if text[i:len(substr)+i] == substr:
        count += 1

print(count)