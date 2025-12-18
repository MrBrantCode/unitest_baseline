"""
QUESTION:
Write a function named `add_hundred_to_numbers` that uses regular expressions to find all numbers in a given string and returns a new string where 100 is added to each of these numbers.
"""

import re

def add_hundred_to_numbers(sentence):
    pattern = r'\d+'
    replacement = lambda match: str(int(match.group()) + 100)
    return re.sub(pattern, replacement, sentence)