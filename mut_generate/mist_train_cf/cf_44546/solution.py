"""
QUESTION:
Write a function `sum_numbers_in_string` that takes a string as input and returns the sum of all numeric values (integers and floating point numbers) in the string, considering both positive and negative numbers.
"""

import re

def sum_numbers_in_string(input_string):
    # Regular expression to match positive/negative/int/float numbers
    numbers = re.findall(r'[-+]?\d*\.\d+|[-+]?\d+', input_string)
    # Convert all extracts to float and sum them up
    return sum(map(float, numbers))