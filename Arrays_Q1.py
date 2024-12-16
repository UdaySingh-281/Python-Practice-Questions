# Write a Python program to create an array of 5 integers and display the array items.
# Access individual element through indexes.

import array as arr

numbers = arr.array('i',[1,2,3,4,5])

for i in numbers:
  print(i, end = " ")