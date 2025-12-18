"""
QUESTION:
Write a function named `format_large_number` that takes an integer as input and returns a string with the number formatted with commas as thousand separators. The function should work with both positive and negative integers, and should not truncate or round the number.
"""

def format_large_number(num):
    """
    Format a large number with commas as thousand separators.
    
    Args:
    num (int): The number to be formatted.
    
    Returns:
    str: The formatted number with commas as thousand separators.
    """
    return "{:,}".format(abs(num)) if num >= 0 else "-{:,}".format(abs(num))