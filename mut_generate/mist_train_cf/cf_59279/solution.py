"""
QUESTION:
Write a function `replace_chars` that takes a string as input and returns the string with all spaces replaced with underscores and '#' replaced with 'm' and '?' replaced with 'r'. The function should handle any input string and be efficient in terms of time complexity.
"""

def replace_chars(input_string):
    return input_string.replace(' ', '_').replace('#', 'm').replace('?', 'r')