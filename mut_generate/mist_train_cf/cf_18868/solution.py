"""
QUESTION:
Write a function `format_number` that takes a float number as input, formats it to two decimal places in scientific notation, and rounds up if the fourth decimal place is greater than or equal to 5.
"""

def format_number(num):
    """
    Format a float number to two decimal places in scientific notation and 
    round up if the fourth decimal place is greater than or equal to 5.

    Args:
        num (float): The input float number.

    Returns:
        str: The formatted number in scientific notation.
    """
    return '{:.2e}'.format(round(float('{:.4e}'.format(num)), 2))