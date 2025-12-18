"""
QUESTION:
Create a function `find_pattern` that takes a list of strings as input and returns a list of strings that end with the consecutive letters "oo" but do not have "o" preceded by the letter "b". The function should use a regular expression to match the pattern.
"""

import re

def find_pattern(strings):
    pattern = r"(?<!b)oo\b"
    matches = [string for string in strings if re.search(pattern, string)]
    return matches