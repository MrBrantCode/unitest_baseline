"""
QUESTION:
Write a function `find_pets` that takes a list of strings as input and returns a list of strings that contain either 'cat' or 'dog'. Use regular expressions to accomplish this task. The function should only return strings that contain 'cat' or 'dog' as a substring, and should be case-sensitive.
"""

import re

def find_pets(strings):
    return [string for string in strings if re.search(r'(cat|dog)', string)]