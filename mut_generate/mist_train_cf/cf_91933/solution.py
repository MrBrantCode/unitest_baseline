"""
QUESTION:
Write a function `extract_numeric_sum` that takes a string as input and returns the sum of all numeric values found in the string. The function should be able to extract integers from the string, and it should not assume any specific format or structure of the input string. The function should return 0 if no numeric values are found in the string.
"""

import re

def extract_numeric_sum(s):
    """
    This function takes a string as input and returns the sum of all numeric values found in the string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of all numeric values found in the string.
    """
    # Use regex to find all numeric values in the string
    numeric_values = re.findall(r'\d+', s)

    # Convert the numeric values to integers and calculate the sum
    return sum(int(value) for value in numeric_values)