"""
QUESTION:
Write a function `convert_base16_to_integer` that takes a string of hexadecimal digits as input and returns its corresponding integer value. The function should work with both uppercase and lowercase letters and handle strings of any length.
"""

def convert_base16_to_integer(string):
    """
    Convert a hexadecimal string to its corresponding integer value.

    This function works with both uppercase and lowercase letters and handles strings of any length.

    Parameters:
    string (str): A string of hexadecimal digits.

    Returns:
    int: The integer value corresponding to the input hexadecimal string.
    """
    hex_digits = "0123456789ABCDEF"
    result = 0
    for digit in string:
        value = hex_digits.index(digit.upper())
        result = result * 16 + value
    return result