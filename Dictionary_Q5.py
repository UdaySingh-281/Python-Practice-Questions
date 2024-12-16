# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary (n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

mydict, n =  dict(), int(input("Enter the range: "))
for i in range(1,n+1):
  mydict[i] = i*i
print(mydict)
     