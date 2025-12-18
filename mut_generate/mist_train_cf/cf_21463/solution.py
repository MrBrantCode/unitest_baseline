"""
QUESTION:
Write a function called `clean_string` that takes a string as input, removes all punctuation marks, and returns the string with all letters in uppercase.
"""

import string

def clean_string(s):
    return s.translate(str.maketrans('', '', string.punctuation)).upper()