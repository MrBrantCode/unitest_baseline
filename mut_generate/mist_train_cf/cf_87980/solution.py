"""
QUESTION:
Design a function named `filter_words` that filters a list of words based on a given set of characters. The function should accept the set of characters as a string, list, or tuple, and the list of words as a list. The function should ignore case, punctuation, and special characters, and should handle duplicate characters in the input. It should return the filtered words in the same order as they appear in the original list, with all non-alphabetic characters removed.
"""

import string

def filter_words(characters, words):
    # Convert characters to a set for efficient membership testing
    characters_set = set(characters.lower())

    # Remove punctuation and special characters from words
    translator = str.maketrans('', '', string.punctuation)
    words = [word.translate(translator) for word in words]

    filtered_words = []
    for word in words:
        # Convert word to lowercase for case-insensitive comparison
        word = word.lower()
        
        # Check if all characters in word are in characters_set
        if all(char in characters_set for char in word):
            filtered_words.append(''.join(filter(str.isalpha, word)))

    return filtered_words