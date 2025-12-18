"""
QUESTION:
Design a function named `filter_words` that filters a list of words based on a given set of characters. The function should accept both a string and a list of characters as input, handle duplicate characters, be case-insensitive, and ignore punctuation or special characters in the words. The function should return the filtered words in their original order.
"""

import string

def filter_words(characters, words):
    if isinstance(characters, str):
        characters = list(characters.lower())
    else:
        characters = [char.lower() for char in characters]

    filtered_words = []

    for word in words:
        word = word.lower()
        word = ''.join(char for char in word if char.isalnum())

        if all(char in characters for char in word):
            filtered_words.append(word)

    return filtered_words