"""
QUESTION:
Write a function called `remove_whitespace` that takes an input string and returns a new string with all whitespace characters removed. The function should eliminate all forms of whitespace, including but not limited to spaces, tabs, and newlines.
"""

def remove_whitespace(input_string):
    return ''.join(input_string.split())