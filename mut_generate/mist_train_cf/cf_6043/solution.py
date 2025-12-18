"""
QUESTION:
Write a function called `extract_numbers` that takes a string as input and returns a list of numeric values extracted from the string. The function should handle negative numbers, floating-point numbers, and scientific notation. The function should also handle strings that contain multiple numbers separated by non-numeric characters. If the input string is empty or does not contain any numeric values, the function should return an empty list.
"""

import re

def extract_numbers(string):
    # Use regular expression to find all numeric values in the string
    numbers = re.findall(r'[-+]?\d*\.\d+|[-+]?\d+', string)
    
    # Convert the numbers from string to numeric values
    numbers = [float(number) if '.' in number else int(number) for number in numbers]
    
    return numbers