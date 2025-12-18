"""
QUESTION:
Write a function `count_words_start_with_letters(string, letters)` that takes a string and a list of letters as input. Using regular expressions, extract words that start with the specified letters and return a dictionary where the keys are the found words and the values are their occurrence counts. The function should be case sensitive and consider punctuation as part of the word.
"""

import re
from collections import Counter

def count_words_start_with_letters(string, letters):
    words = re.findall(r'\b[' + ''.join(letters) + r']\w*', string)
    return dict(Counter(words))