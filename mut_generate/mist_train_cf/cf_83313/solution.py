"""
QUESTION:
Write a function `separate_characters` that takes a list of strings as input, where each string consists of either numeric characters or alphabetic characters. The function should return two lists: one containing the numeric strings and the other containing the alphabetic strings. The function should use regular expressions to distinguish between numeric and alphabetic strings.
"""

import re

def separate_characters(input_list):
    """
    This function separates a list of strings into two lists, 
    one containing numeric strings and the other containing alphabetic strings.

    Args:
        input_list (list): A list of strings where each string consists of either numeric characters or alphabetic characters.

    Returns:
        tuple: A tuple containing two lists, the first list contains numeric strings and the second list contains alphabetic strings.
    """
    numeric_pattern = re.compile('^[0-9]+$')
    alpha_pattern = re.compile('^[a-zA-Z]+$')

    numeric_list = [item for item in input_list if numeric_pattern.match(item)]
    alpha_list = [item for item in input_list if alpha_pattern.match(item)]

    return numeric_list, alpha_list