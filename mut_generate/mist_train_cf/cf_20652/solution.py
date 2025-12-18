"""
QUESTION:
Write a function named `extract_numeric_values` that takes a string as input and returns a list of all numeric values (including negative numbers, floating-point numbers, and numbers in scientific notation) found in the string as floats. The function should be able to handle strings containing multiple numbers separated by non-numeric characters.
"""

import re

def extract_numeric_values(string):
    # Remove all non-numeric characters except for '.', '-' and 'e'
    cleaned_string = re.sub(r'[^0-9.\-e]', '', string)

    # Extract all numeric values from the cleaned string
    numeric_values = re.findall(r'-?\d+(?:\.\d+)?(?:[eE]-?\d+)?', cleaned_string)

    return [float(value) for value in numeric_values]