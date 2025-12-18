"""
QUESTION:
Create a function named `remove_whitespace` that takes a string `s` as input and returns a new string where all whitespace characters, including spaces, tabs, and newline characters, have been removed.
"""

def remove_whitespace(s):
    return ''.join(ch for ch in s if not ch.isspace())