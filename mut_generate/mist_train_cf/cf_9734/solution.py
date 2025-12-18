"""
QUESTION:
Write a function `extract_numbers` that takes a string as input and returns a list of numbers greater than 5 that are found in the string, but only if the string contains at least one special character. The function should use the `re` module to extract numbers and special characters from the string.
"""

import re

def extract_numbers(input_string):
    """
    Extracts numbers greater than 5 from the input string if it contains at least one special character.

    Args:
        input_string (str): The input string to extract numbers from.

    Returns:
        list: A list of numbers greater than 5 if the string contains at least one special character, otherwise an empty list.
    """
    numbers = re.findall(r'\b(\d+)\b', input_string)  # find all numbers
    special_characters = re.findall(r'\W', input_string)  # find all special characters

    return [int(num) for num in numbers if int(num) > 5 and special_characters]