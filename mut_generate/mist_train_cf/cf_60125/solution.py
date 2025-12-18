"""
QUESTION:
Write a function `count_occurrences` that takes an input string and returns the number of occurrences of the standalone sequence "py" (case-insensitive) in the string, where "py" is not part of another word.
"""

import re

def count_occurrences(input_string):
    pattern = re.compile(r'\bpy\b', re.IGNORECASE)
    matches = pattern.findall(input_string)
    return len(matches)