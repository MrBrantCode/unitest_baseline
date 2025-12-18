"""
QUESTION:
Create a function named `count_ab_occurrences` that takes a string as input and returns the number of occurrences of the letter "a" immediately followed by the letter "b" in the string, ignoring case sensitivity.
"""

import re

def count_ab_occurrences(string):
    pattern = r'ab'
    count = len(re.findall(pattern, string, re.IGNORECASE))
    return count