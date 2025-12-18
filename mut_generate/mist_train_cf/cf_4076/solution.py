"""
QUESTION:
Create a function called `format_output` that takes a floating point number as input, multiplies it by 100, rounds to the nearest integer, and then formats it in scientific notation with exactly two decimal places, rounding up if the fourth decimal place is greater than or equal to 5.
"""

import math

def format_output(num):
    """
    Format a floating point number by multiplying it by 100, rounding to the nearest integer, 
    and then formatting it in scientific notation with exactly two decimal places, 
    rounding up if the fourth decimal place is greater than or equal to 5.

    Args:
        num (float): The floating point number to format.

    Returns:
        str: The formatted string.
    """
    return '{:.2e}'.format(round(num * 100))