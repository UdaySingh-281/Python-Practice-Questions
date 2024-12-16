# Write a Python function that takes a list of words and returns the length of the longest one.

def func_max_len_word(words):
    max_word, word_ = float('-inf'), ""
    for word in words:
        if len(word) > max_word:
            max_word = len(word)
            word_ = word
    return word_, max_word

print(func_max_len_word(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))