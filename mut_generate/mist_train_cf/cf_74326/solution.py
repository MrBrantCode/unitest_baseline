"""
QUESTION:
Write a function named `find_xy_sequence` that takes a string `text` as input and returns all occurrences of 'x' immediately followed by 'y' in the given text, regardless of other characters present in the text. The function should be case sensitive.
"""

import re

def find_xy_sequence(text):
    pattern = 'xy'
    matches = re.findall(pattern, text)
    return matches