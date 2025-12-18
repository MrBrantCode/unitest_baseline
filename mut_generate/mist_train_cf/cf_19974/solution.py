"""
QUESTION:
Count the number of whole-word occurrences of a given pattern in a string. The pattern can be case-sensitive and contain special characters. Write a function named `count_pattern_occurrences` that takes two parameters: the input string `text` and the `pattern` to be searched.
"""

import re

def count_pattern_occurrences(text, pattern):
    pattern = r'\b' + re.escape(pattern) + r'\b'
    occurrences = re.findall(pattern, text)
    return len(occurrences)