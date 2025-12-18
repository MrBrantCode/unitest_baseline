"""
QUESTION:
Write a function named `contains_only_numeric_values` that takes a string as input and returns `True` if the string contains only numeric values, and `False` otherwise. The function should use the `isdigit` method of the `str` object in Python.
"""

def contains_only_numeric_values(input_string):
    """
    Checks if a given string contains only numeric values.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the string contains only numeric values, False otherwise.
    """
    return input_string.isdigit()