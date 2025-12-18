"""
QUESTION:
Write a function named `unique_words_in_alphabetical_order` that takes a string as input and returns a list of all unique words in alphabetical order. The function should be case-insensitive and have a time complexity of O(n^2), where n is the length of the string. It should not use any built-in sorting functions or data structures.
"""

def unique_words_in_alphabetical_order(str):
    words = str.lower().split()
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    sorted_words = []
    while unique_words:
        min_word = unique_words[0]
        for word in unique_words:
            if word < min_word:
                min_word = word
        sorted_words.append(min_word)
        unique_words.remove(min_word)
    return sorted_words