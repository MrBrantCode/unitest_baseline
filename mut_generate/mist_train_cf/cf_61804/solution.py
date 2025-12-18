"""
QUESTION:
Write a function `sum_numbers` that takes a string `s` as input and returns the sum of all numbers found in the string. The function should consider negative numbers and numbers with decimals. It should ignore special characters and words in the string. The input string may contain numbers expressed in scientific notation and may have numbers with commas, leading decimal points, or negative signs without a space.
"""

import re

def sum_numbers(s):
    numbers = re.findall('[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', s)
    numbers = [float(num.replace(',', '')) for num in numbers]
    return sum(numbers)