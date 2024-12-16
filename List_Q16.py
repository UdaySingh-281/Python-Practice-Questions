# Function to split a list based on the first character of words
def split_list_based_on_first_char(word_list):
    grouped_words = {}

    for word in word_list:
        first_char = word[0].upper()

        if first_char not in grouped_words:
            grouped_words[first_char] = []

        grouped_words[first_char].append(word)

    return list(grouped_words.values())


word_list = ["apple", "banana", "apricot", "cherry", "carrot", "blueberry"]

split_list = split_list_based_on_first_char(word_list)

print("Split list based on first character of word:", split_list)
