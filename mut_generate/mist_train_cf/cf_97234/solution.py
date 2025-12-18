"""
QUESTION:
Write a function `word_count(string)` that returns a dictionary containing the number of occurrences of each unique word in the given string. The function should consider all possible cases, including uppercase and lowercase letters, and ignore punctuation marks and special characters. The function should handle edge cases like empty strings and multiple spaces between words.
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