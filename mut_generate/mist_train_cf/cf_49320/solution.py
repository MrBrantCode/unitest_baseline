"""
QUESTION:
Write a function called `dec_to_hex` that converts a given decimal number into its corresponding hexadecimal notation. The function should accept an integer as input and return a string representing the hexadecimal equivalent. The hexadecimal digits should be in uppercase.
"""

def dec_to_hex(dec):
    """
    Converts a given decimal number into its corresponding hexadecimal notation.

    Args:
    dec (int): The decimal number to be converted.

    Returns:
    str: A string representing the hexadecimal equivalent in uppercase.
    """
    return "{0:x}".format(int(dec)).upper()