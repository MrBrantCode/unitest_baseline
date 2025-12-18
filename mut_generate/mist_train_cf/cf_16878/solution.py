"""
QUESTION:
Write a function named `convert_string_to_list` that takes a string as input, removes non-alphabetic characters and punctuation marks, and returns a list of the remaining characters. The function should handle strings containing alphabets, spaces, and special characters.
"""

import string

def convert_string_to_list(s):
    return [char for char in s if char.isalpha() or char.isspace()]