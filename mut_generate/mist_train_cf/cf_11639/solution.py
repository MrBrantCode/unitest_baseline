"""
QUESTION:
Write a Python function named `extract_numeric_sum` that takes a string as input and returns the sum of all numeric values found in the string. The function should be able to extract integers from the string, regardless of their position or context. The input string may contain non-numeric characters and may not contain any numeric values, in which case the function should return 0.
"""

import re

def extract_numeric_sum(input_string):
    """
    This function takes a string as input and returns the sum of all numeric values found in the string.

    Args:
    input_string (str): The input string from which to extract numeric values.

    Returns:
    int: The sum of all numeric values found in the string. If no numeric values are found, returns 0.
    """
    
    # Use regex to find all numeric values in the string
    numeric_values = re.findall(r'\d+', input_string)
    
    # Convert the numeric values to integers and calculate the sum
    total_sum = sum(int(value) for value in numeric_values)
    
    return total_sum