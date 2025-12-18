"""
QUESTION:
Write a function `remove_non_numeric_chars` that takes a string as input and returns a new string containing only the numeric characters from the original string.
"""

def remove_non_numeric_chars(s):
    return ''.join(filter(str.isdigit, s))