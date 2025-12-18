"""
QUESTION:
Create a function named `clean_string` that takes a string `s` as input and returns the string with all whitespace characters and special characters removed. The function should be able to handle any type of whitespace character (e.g., spaces, tabs, newline characters) and special character (e.g., punctuation marks, symbols).
"""

import re

def clean_string(s):
    s = re.sub(r'\s', '', s)
    s = re.sub(r'\W', '', s)
    return s