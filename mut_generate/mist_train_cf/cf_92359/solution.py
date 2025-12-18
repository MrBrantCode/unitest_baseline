"""
QUESTION:
Write a function named `remove_parentheses` that takes a string as input and returns the string with all pairs of parentheses and the words inside them removed. The function should handle strings with multiple pairs of nested parentheses.
"""

import re

def remove_parentheses(s):
    return re.sub(r'\([^)]*\)', '', s)