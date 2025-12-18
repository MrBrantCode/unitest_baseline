"""
QUESTION:
Write a function `hex_equivalent` that takes a string representation of a decimal number as input and returns its equivalent hexadecimal representation as a string, excluding the '0x' prefix.
"""

def hex_equivalent(num_string):
    """
    Convert a decimal number string into its hexadecimal representation.

    Args:
        num_string (str): A string representation of a decimal number.

    Returns:
        str: The hexadecimal representation of the input decimal number, excluding the '0x' prefix.
    """
    return hex(int(num_string))[2:]