"""
QUESTION:
Write a function `unique_words_with_length_greater_than_three` that takes a string as input and returns a list of unique words with a length greater than three. The function should be case insensitive and ignore punctuation. The time complexity should be O(n), where n is the length of the input string, and the input string can be up to 10^6 characters long.
"""

import string

def unique_words_with_length_greater_than_three(text):
    unique_words = set()
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    
    for word in words:
        if len(word) > 3 and word not in unique_words:
            unique_words.add(word)
    
    return list(unique_words)