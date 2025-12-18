"""
QUESTION:
Write a function `truncate_number` that takes a floating-point number as input and returns the decimal segment of the number. The decimal segment is the residual portion that is always less than 1.
"""

import math

def truncate_number(number):
    """
    This function takes a floating-point number as input and returns the decimal segment of the number.
    
    Parameters:
    number (float): The input floating-point number.
    
    Returns:
    float: The decimal segment of the number.
    """
    return number - math.floor(number)