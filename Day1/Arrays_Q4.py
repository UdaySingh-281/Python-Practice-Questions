# Write a Python program to remove the first occurrence of a specified element from an array.

def remove_elemnt(numbers, target):
  for i in numbers:
    if i == target:
      numbers.remove(i)
      break
  return numbers

remove_elemnt([1,2,3,4,5,6,7,8,9,10], 1)