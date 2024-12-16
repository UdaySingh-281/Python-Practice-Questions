# Write a Python program to get the number of occurrences of a specified element in an array.

def occurrences(numbers, target, count = 0):
  for i in numbers:
    if i == target:
      count += 1
  return count

occurrences([1,2,3,4,5,6,7,8,9,10], 1)