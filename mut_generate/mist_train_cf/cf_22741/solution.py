"""
QUESTION:
Create a function called `word_count` that takes a string as input and returns a dictionary containing the number of occurrences of each unique word in the string, considering all possible cases including uppercase and lowercase letters and ignoring punctuation marks and special characters. The function should handle edge cases like empty strings and multiple spaces between words.
"""

import re

def word_count(string):
    string = re.sub(r'[^\w\s]', '', string)
    words = string.split()
    word_counts = {}

    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts