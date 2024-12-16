# Write a Python program to add 'ing' at the end of a given string (length should be at # least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the

# given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

mystr = input("Enter the string: ")

if len(mystr) >= 3 and "ing" not in mystr:
    mystr += "ing" 

elif mystr[-1:-4] in "ing":
    mystr += "ly"

print(mystr)
