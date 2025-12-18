"""
QUESTION:
Write a function `convert_and_invert(n)` that takes an integer `n` as input and returns its hexadecimal representation in base 16 as a string, inverted, handling both positive and negative integers. The hexadecimal representation should exclude the '0x' prefix for positive numbers and the '-0x' prefix for negative numbers.
"""

def convert_and_invert(n):
    """
    Converts an integer to its hexadecimal representation in base 16 as a string, 
    inverted, handling both positive and negative integers.

    Args:
        n (int): The integer to convert.

    Returns:
        str: The inverted hexadecimal representation of the input integer.
    """
    if n < 0:
        return '-' + hex(n)[3:][::-1]
    else:
        return hex(n)[2:][::-1]