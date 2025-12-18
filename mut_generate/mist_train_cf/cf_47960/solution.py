"""
QUESTION:
Implement a function `count_unique_words(s)` that takes a string of alphanumeric characters as input and returns the number of unique words in the string. 

The function should consider the following rules:
- The words may have non-alphanumeric prefixes and/or suffixes that should be stripped off during counting.
- The words are case-sensitive.
- Non-alphanumeric characters within a word should be treated as separators.
- The function should be efficient to handle strings up to 10^6 characters.
- Repeated words should be counted as one unique word.
"""

import re

def count_unique_words(s):
    words = re.split("\W+", s)
    return len(set(words))