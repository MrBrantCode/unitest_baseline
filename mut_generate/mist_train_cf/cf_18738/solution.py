"""
QUESTION:
Write a function named `sum_of_numeric_values` that takes a string as input and returns the sum of all numeric values found in the string. The function should be implemented in a single line of code and should be able to handle strings containing multiple occurrences of numeric values.
"""

import re

def sum_of_numeric_values(string):
    return sum(map(int, re.findall(r'\d+', string)))