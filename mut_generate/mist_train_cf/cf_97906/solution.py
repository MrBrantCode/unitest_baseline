"""
QUESTION:
Write a function called `find_pets` that takes a list of strings as input and returns a list of strings that contain either 'cat' or 'dog'. Use regular expressions in your solution. The function should not take any additional arguments besides the list of strings.
"""

import re

def find_pets(strings):
    return [string for string in strings if re.search(r'(cat|dog)', string)]