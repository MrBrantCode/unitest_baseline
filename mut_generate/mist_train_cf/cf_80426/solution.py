"""
QUESTION:
Extract all numeric values from a given string.

Write a function called `extract_numbers` that takes a string as input, and returns a list of integers representing the numeric values found in the string. The function should be able to find one or more consecutive digits within the string and convert them into integers.

Restrictions: The function should only return a list of integers and should not include any non-numeric values from the input string.
"""

import re

def extract_numbers(s):
    # Find all numeric values using a regex pattern
    numbers = re.findall(r'\d+', s)

    # Convert the string values to integers
    return [int(num) for num in numbers]