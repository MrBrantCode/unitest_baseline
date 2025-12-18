"""
QUESTION:
Write a function `hex_to_oct` to convert a given hexadecimal number to an octal number. The function should take a string representing a hexadecimal number as input, convert it to a decimal number, then to an octal number, and return the octal number as a string. The returned octal number should not have the '0o' prefix.
"""

def hex_to_oct(hex_num):
    """
    This function converts a given hexadecimal number to an octal number.

    Args:
        hex_num (str): A string representing a hexadecimal number.

    Returns:
        str: The octal number as a string without the '0o' prefix.
    """
    dec_num = int(hex_num, 16)
    return oct(dec_num)[2:]