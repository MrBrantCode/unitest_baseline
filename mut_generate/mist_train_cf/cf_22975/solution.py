"""
QUESTION:
Write a function `reverse_string` that takes a string as input, removes all whitespace characters and non-alphabetic characters (including punctuation marks, special characters, and numbers), and reverses the remaining characters in place. The function should handle both uppercase and lowercase characters and return the resulting string.
"""

import re

def reverse_string(s):
    s = re.sub(r'\s', '', s)
    s = re.sub(r'[^A-Za-z]', '', s)
    s = s[::-1]
    return s