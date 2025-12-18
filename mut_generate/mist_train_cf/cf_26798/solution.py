"""
QUESTION:
Implement the function `count_unique_words(input_string)` that takes a string as input and returns a dictionary containing the count of each unique word in the string. The function should ignore case and punctuation, treating words with different capitalization as the same word, and only consider alphanumeric characters as part of a word.
"""

import re

def entrance(input_string):
    word_count = {}
    words = re.findall(r'\b\w+\b', input_string.lower())
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count