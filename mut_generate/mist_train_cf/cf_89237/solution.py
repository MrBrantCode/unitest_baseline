"""
QUESTION:
Create a Python function named `extract_numbers` that takes a string as input and returns a list of numeric values. The function should handle negative numbers, floating-point numbers, and scientific notation, and it should be able to extract multiple numbers separated by non-numeric characters. The output list should contain numeric values (int or float) and should be empty if the input string does not contain any numeric values.
"""

import re

def extract_numbers(string):
    # Use regular expression to find all numeric values in the string
    numbers = re.findall(r'[-+]?\d*\.\d+|[-+]?\d+', string)
    
    # Convert the numbers from string to numeric values
    numbers = [float(number) if '.' in number else int(number) for number in numbers]
    
    return numbers