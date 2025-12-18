"""
QUESTION:
Create a function `extract_unique_numbers` that takes a string as input, extracts all unique numbers from the string, and returns them as a set. The function should ignore any duplicate numbers.
"""

import re

def extract_unique_numbers(string):
    numbers = re.findall(r'\d+', string)
    unique_numbers = set()
    for number in numbers:
        unique_numbers.add(int(number))
    return unique_numbers