"""
QUESTION:
Write a function `count_word_occurrences` that takes a string and a list of strings as input. The function should return the number of times the input string occurs as a whole word in any of the strings in the list, ignoring case sensitivity, and considering the possibility of the string being surrounded by special characters or punctuation marks.
"""

import re

def count_word_occurrences(string, arr):
    pattern = r'\b' + re.escape(string) + r'\b'
    count = 0
    for s in arr:
        if re.search(pattern, s, re.IGNORECASE):
            count += 1
    return count