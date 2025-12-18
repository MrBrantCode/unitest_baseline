"""
QUESTION:
Write a function `get_length` that takes a string as input and returns the number of alphanumeric characters in the string, excluding whitespace characters and punctuation marks.
"""

import string

def get_length(s):
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.replace(" ", "")
    return sum(char.isalnum() for char in s)