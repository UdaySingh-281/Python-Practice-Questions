# Write a Python program to find the list of words that are longer than n from a given list of words.

def words_longer_than_n(word_list, n):
    result = [word for word in word_list if len(word) > n]
    return result

word_list = ['apple', 'banana', 'cherry', 'kiwi', 'pear', 'orange']

n = 5

long_words = words_longer_than_n(word_list, n)

print("Words longer than", n, "characters:", long_words)