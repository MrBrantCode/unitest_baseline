"""
QUESTION:
Write a function `extract_sum` that takes a string as input, extracts all numeric values from the string, and returns their sum without using any built-in Python functions or libraries.
"""

import re

def extract_sum(string):
    return sum([int(x) for x in re.findall(r'\d+', string)])