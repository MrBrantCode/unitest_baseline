"""
QUESTION:
Develop a function `find_adverb` that takes a string as input and returns the first word ending with 'ly', along with its start and end indices within the string. If no such word is found, return None.
"""

import re

def find_adverb(string):
    words = string.split(" ")
    for word in words:
        if word.endswith('ly'):
            pure_word = re.sub(r'\W+', '', word)
            start = string.index(pure_word)
            end = start + len(pure_word) - 1
            return (pure_word, start, end)
    return None