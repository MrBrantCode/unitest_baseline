"""
QUESTION:
Create a function named `count_words` that takes a list of words as input, where the list may contain duplicates and special characters. The function should return a dictionary where the keys are unique words (after removing special characters and considering case insensitivity) and the values are lists containing the total occurrences and the number of letters in the word. The function should ignore words that contain digits and special characters combined.
"""

import string
import re

def count_words(word_list):
    # Pattern to identify words with letters only (no digits, no special characters)
    pattern = re.compile('^[a-zA-Z]+$')

    # Initialize empty dictionary
    word_dict = {}

    for word in word_list:
        # Strip special characters and convert to lower
        stripped_word = re.sub('['+string.punctuation+']', '', word).lower()

        # If word contains only letters
        if pattern.match(stripped_word):
            # If word is already in dictionary, increment count
            if stripped_word in word_dict.keys():
                word_dict[stripped_word][0] += 1
            # If word is not in dictionary, add it with count 1 and length of word
            else:
                word_dict[stripped_word] = [1, len(stripped_word)]

    return word_dict