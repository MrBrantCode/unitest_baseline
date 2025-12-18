"""
QUESTION:
Write a function `separate_key_value_pairs` that takes a string of three "key=value" pairs separated by commas and spaces as input and returns a string of the same pairs enclosed in parentheses, separated by a comma and a space. The keys and values contain only alphanumeric characters and are separated by an equal sign. The number of pairs is always three, but their order may vary.
"""

import re

def separate_key_value_pairs(input_string):
    """
    This function takes a string of three "key=value" pairs separated by commas and spaces,
    and returns a string of the same pairs enclosed in parentheses, separated by a comma and a space.

    Args:
        input_string (str): A string of three "key=value" pairs separated by commas and spaces.

    Returns:
        str: A string of the same pairs enclosed in parentheses, separated by a comma and a space.
    """
    parts = re.split(", ", input_string)
    output_string = "(" + "), (".join(parts) + ")"
    return output_string