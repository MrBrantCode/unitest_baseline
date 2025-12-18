"""
QUESTION:
Write a function `extract_numeric_values` that takes a string as input and returns a list of numeric values (including negative numbers and floating-point numbers) found in the string. The function should extract all numeric values and convert them to floats.
"""

import re

def extract_numeric_values(string):
    pattern = r'[-+]?\d*\.\d+|[-+]?\d+'
    matches = re.findall(pattern, string)
    return [float(match) for match in matches]