"""
QUESTION:
Write a function called `convert_to_floats` that takes a string of space-separated numbers as input. The function should return a list of floats, ignoring any invalid characters or numbers, and handling cases with missing or extra spaces between numbers.
"""

import re

def convert_to_floats(input_string):
    """
    Converts a string of space-separated numbers into a list of floats, 
    ignoring any invalid characters or numbers, and handling cases with 
    missing or extra spaces between numbers.

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
    return [float(number) for number in numbers if number.replace('.', '', 1).isdigit()]