"""
QUESTION:
Write a function `count_words(string)` that takes a string of up to 1 million characters as input, removes any punctuation marks and special characters, and returns a dictionary where the keys are the unique words with at least three characters (considering case-sensitive) and the values are their corresponding counts.
"""

import re

def count_words(string):
    # Remove punctuation marks and special characters
    string = re.sub(r'[^\w\s]', '', string)

    # Split the string into words
    words = string.split()

    # Count the occurrences of each word
    word_count = {}
    for word in words:
        # Consider only words that are at least three characters long
        if len(word) >= 3:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count