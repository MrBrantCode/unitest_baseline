"""
QUESTION:
Write a function `add_hundred_to_numbers` that takes a string as input, uses regular expressions to find all sequences of digits in the string, and returns a new string where each sequence of digits has 100 added to it.
"""

import re

def add_hundred_to_numbers(sentence):
    pattern = r'\d+'
    replacement = lambda match: str(int(match.group()) + 100)
    return re.sub(pattern, replacement, sentence)