"""
QUESTION:
Write a function named `extract_unique_numbers` that takes a string as input and returns a set of unique numbers found in the string. The function should ignore any duplicate numbers.
"""

import re

def extract_unique_numbers(string):
    numbers = re.findall(r'\d+', string)
    unique_numbers = set()
    for number in numbers:
        unique_numbers.add(int(number))
    return unique_numbers