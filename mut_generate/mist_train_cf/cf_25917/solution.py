"""
QUESTION:
Write a function named decimal_to_hexadecimal that takes an integer decimal number as input and returns its hexadecimal representation. The function should return the hexadecimal representation in the format '0xXXXX', where XXXX is the hexadecimal value.
"""

def decimal_to_hexadecimal(n):
    """
    This function converts a decimal number into its hexadecimal representation.

    Args:
        n (int): A decimal number.

    Returns:
        str: The hexadecimal representation of the decimal number in the format '0xXXXX'.
    """
    return hex(n)