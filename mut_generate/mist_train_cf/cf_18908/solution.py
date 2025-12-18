"""
QUESTION:
Write a function named `parse_input` that takes a string input in the format 'x - value, y - value' where value can be any number in the range -10^9 to 10^9 in either decimal or scientific notation format. The function should return the values of x and y as a tuple. The time complexity should be O(1) and the space complexity should be O(1).
"""

import re

def parse_input(input_string):
    """
    Parse the input string in the format 'x - value, y - value' and return the values of x and y as a tuple.

    Args:
        input_string (str): The input string in the format 'x - value, y - value'

    Returns:
        tuple: A tuple containing the values of x and y
    """
    # Regex pattern to match the input format
    pattern = r'x - (-?\d+\.?\d*(?:e[+-]?\d+)?)\s*,\s*y - (-?\d+\.?\d*(?:e[+-]?\d+)?)'

    # Extract the values of x and y from the input string using regex
    match = re.match(pattern, input_string)
    if match:
        x = float(match.group(1))
        y = float(match.group(2))
        return x, y
    else:
        return None, None