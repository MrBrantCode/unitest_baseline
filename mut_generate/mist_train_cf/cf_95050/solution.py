"""
QUESTION:
Write a function named `count_word_occurrences` that takes a string and a list of strings as input and returns the number of times the string occurs as a whole word in the list, ignoring case sensitivity and considering special characters or punctuation marks.
"""

import re

def count_word_occurrences(string, arr):
    count = 0
    pattern = r"\b" + re.escape(string) + r"\b"
    for s in arr:
        if re.search(pattern, s, re.IGNORECASE):
            count += 1
    return count