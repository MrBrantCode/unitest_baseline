"""
QUESTION:
Write a function called `find_numbers` that takes a string `text` as input and returns a list of all numbers in the string, excluding zero. The function should use a Regular Expression pattern to identify the numbers.
"""

import re

def find_numbers(text):
    pattern = re.compile(r'[1-9]\d*')
    return pattern.findall(text)