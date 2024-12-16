# Write a Python program to print a dictionary in table format.

mydict = {'C1':[1,2,3],'C2':[4,5,6],'C3':[7,8,9]}

for key, value in mydict.items():
  print(key, end = " ")
  for i in value:
    print(i, end = " ")
  print()
