# 3. Write a Python program to get a string from a given string where all occurrences of its
# first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

mystr = input("Enter the string: ")
newstr = str()

char_to_be_replaced = mystr[0]

for i in range(0, len(mystr)):
    if mystr[i] == char_to_be_replaced and i != 0:
        newstr += '$'
        continue
    newstr += mystr[i]

print(newstr)