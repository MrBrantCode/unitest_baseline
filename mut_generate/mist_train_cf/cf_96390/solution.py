"""
QUESTION:
Write a function `count_ab_occurrences(string)` that counts the number of occurrences of the letter "a" followed by the letter "b" in the given string. The letters "a" and "b" must be in the same order and adjacent to each other, and the function should be case-insensitive. The input string may contain uppercase and lowercase letters, spaces, punctuation marks, and special characters.
"""

import re

def count_ab_occurrences(string):
    pattern = r'ab'
    count = len(re.findall(pattern, string, re.IGNORECASE))
    return count