"""
QUESTION:
Create a function named `extract_last_five` that takes a list of strings as input and returns a list of strings where each string is the last 5 characters of the corresponding input string. The function should exclude any strings that contain letters or special characters.
"""

import re

def extract_last_five(strings):
    """
    This function takes a list of strings as input, filters out strings with non-numeric characters,
    and returns a list of strings where each string is the last 5 characters of the corresponding input string.

    Args:
        strings (list): A list of strings.

    Returns:
        list: A list of strings where each string is the last 5 characters of the corresponding input string.
    """

    # use list comprehension to filter out non-numeric strings and extract the last 5 characters
    return [value[-5:] for value in strings if re.search('[^0-9]', value) is None]