"""
QUESTION:
Write a function `extract_unique_numbers` that takes a string as input and returns a list of unique numbers found in the string in ascending order. The function should consider a number as a sequence of digits (0-9) and optional decimal point (.) or negative sign (-) at the beginning, and ignore any duplicate numbers.
"""

import re

def extract_unique_numbers(string):
    numbers = re.findall(r"[-+]?\d*\.?\d+", string)
    numbers = [float(number) if '.' in number else int(number) for number in numbers]
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers