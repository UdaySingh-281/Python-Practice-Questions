# Write a Python program to count number of items in a dictionary value that is a list.

mydict = {'C1':[1,2,3],'C2':[4,5,6],'C3':[7,8,9]}
count = 0
for i in mydict.values():
  if type(i) == list:
    count+=1
print(count)
     