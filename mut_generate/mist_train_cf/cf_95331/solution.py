"""
QUESTION:
Write a function called `sum_of_numeric_values` that takes a string as input, extracts all numeric values from the string, and returns their sum. The function should be implemented in a single line of code.
"""

import re

def sum_of_numeric_values(string):
    return sum(map(int, re.findall(r'\d+', string)))