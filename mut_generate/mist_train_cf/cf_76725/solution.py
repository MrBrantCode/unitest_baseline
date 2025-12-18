"""
QUESTION:
Create a function named `find_numerals` that takes a string `text` as input and returns a list of integers. The function should find all numerals exceeding zero within the input string and return them as integers. The function should use a regular expression pattern to match the numerals.
"""

import re

def find_numerals(text):
    pattern = r"([1-9]\d*)"
    matches = re.findall(pattern, text)
    return [int(match) for match in matches]