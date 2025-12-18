"""
QUESTION:
Write a function `convert_to_floats` that takes a string of space-separated numbers as input and returns a list of floats. The function should handle strings that contain invalid characters, missing or extra spaces between numbers, and ignore any invalid numbers in the string.
"""

import re

def convert_to_floats(input_string):
    """
    Convert a string of space-separated numbers to a list of floats.
    
    The function handles strings that contain invalid characters, missing or extra spaces between numbers,
    and ignores any invalid numbers in the string.

    Args:
        input_string (str): A string of space-separated numbers.

    Returns:
        list: A list of floats.
    """
    
    # Remove extra spaces between numbers
    input_string = re.sub(r'\s+', ' ', input_string)
    
    # Remove any non-digit or non-space characters
    input_string = re.sub(r'[^\d\s.]', '', input_string)
    
    # Split the string into individual numbers
    numbers = input_string.split()
    
    # Convert each number to float and return the list
    return [float(number) for number in numbers if number.replace('.', '', 1).replace('-', '', 1).isdigit()]