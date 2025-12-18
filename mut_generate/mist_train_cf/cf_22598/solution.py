"""
QUESTION:
Create a function `extract_unique_numbers` that takes a string as input and returns a list of unique numbers found in the string. A number is defined as a sequence of digits (0-9) and optional decimal point (.) or negative sign (-) at the beginning. The function should ignore any duplicate numbers and return the unique numbers in ascending order.
"""

import re

def extract_unique_numbers(string):
    numbers = re.findall(r"[-+]?\d*\.?\d+", string)
    numbers = [float(number) if '.' in number else int(number) for number in numbers]
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers