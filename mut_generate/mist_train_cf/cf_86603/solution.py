"""
QUESTION:
Write a function called `get_max_length_strings` that takes a list of strings as input, excludes strings containing special characters or numbers, and returns a list of strings with the maximum length. The maximum length of any individual string should not exceed 50 characters. If there are multiple strings with the same maximum length, return all of them in alphabetical order. If the input list is empty, return an empty list.

Note: The function should also calculate and return the average length of all the strings that meet the criteria.
"""

import re

def get_max_length_strings(strings):
    """
    This function takes a list of strings, excludes strings containing special characters or numbers,
    and returns a list of strings with the maximum length. The maximum length of any individual string
    should not exceed 50 characters. If there are multiple strings with the same maximum length,
    return all of them in alphabetical order. If the input list is empty, return an empty list.

    Args:
        strings (list): A list of strings.

    Returns:
        list: A list of strings with the maximum length, along with their average length.
    """

    max_length = 0
    valid_strings = []

    # Find the maximum length of valid strings
    for string in strings:
        if bool(re.match('^[a-zA-Z\s]+$', string)) and len(string) <= 50:
            max_length = max(max_length, len(string))

    # Get all the valid strings with maximum length
    for string in strings:
        if bool(re.match('^[a-zA-Z\s]+$', string)) and len(string) <= 50 and len(string) == max_length:
            valid_strings.append(string)

    # Calculate the average length of valid strings
    average_length = sum(len(string) for string in valid_strings) / len(valid_strings) if valid_strings else 0

    return sorted(valid_strings), average_length