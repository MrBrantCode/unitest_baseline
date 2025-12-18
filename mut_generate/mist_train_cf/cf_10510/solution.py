"""
QUESTION:
Write a function named `get_data_type` that determines the data type for a given value using regular expressions. The function should take a single argument `value` and return its corresponding data type.
"""

def get_data_type(value):
    """
    Returns the data type of the given value.
    
    Args:
    value: The value to determine the data type for.
    
    Returns:
    str: The data type of the given value.
    """
    return type(value).__name__