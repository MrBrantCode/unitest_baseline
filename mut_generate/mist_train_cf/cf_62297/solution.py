"""
QUESTION:
Write a function `alphanumeric_progressions` that takes a string as input and returns a tuple of two strings: one containing all alphanumeric characters from the input string in the order they appear, and another containing all non-alphanumeric characters from the input string in the order they appear.
"""

import string

def alphanumeric_progressions(input_str):
    alnum_chars = ""       # To store grouped alphanumeric characters
    not_alnum_chars = ""   # To store grouped non-alphanumeric characters

    # Iterating over the string
    for char in input_str:
        # If character is alphanumeric, add it to alnum_chars
        if char.isalnum():
            alnum_chars += char
        # If character is not alphanumeric, add it to not_alnum_chars
        else:
            not_alnum_chars += char

    return alnum_chars, not_alnum_chars