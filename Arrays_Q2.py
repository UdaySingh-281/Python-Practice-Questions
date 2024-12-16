# Write a Python program to reverse the order of the items in the array.

import array as arr

numbers = arr.array('i',[1,2,3,4,5])

for i in range(-1, -len(numbers)-1,-1):
  print(numbers[i], end = " ")
print()

print("OR ANOTHER APPROACH WILL BE")
for i in reversed(numbers):
  print(i, end = " ")
     