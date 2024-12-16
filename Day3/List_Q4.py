# Counting the number of strings with length 2 or more and first and last character the same
sample_list = ['abc', 'xyz', 'aba', '1221']
count = 0
for string in sample_list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1
print("Number of strings where the length is 2 or more and the first and last character are the same:", count)
