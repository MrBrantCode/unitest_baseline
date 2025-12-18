"""
QUESTION:
Write a function called `replace_consecutive_spaces` that takes a text string as input and returns the string with all instances of double or more consecutive spaces replaced with a single space.
"""

import re

def replace_consecutive_spaces(text_string):
    return re.sub(' +', ' ', text_string)