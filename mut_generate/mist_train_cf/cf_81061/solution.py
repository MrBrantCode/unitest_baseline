"""
QUESTION:
Write a function called `flip_string` that takes a string `s` as input. The function should remove all punctuation from the string and then reverse the resulting string. The input string can contain any characters, including special symbols.
"""

import string
import re

def flip_string(s):
    # Remove punctuation
    s = re.sub('['+string.punctuation+']', '', s)
    # Flip string
    s = s[::-1]
    return s