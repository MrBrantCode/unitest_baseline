"""
QUESTION:
Convert a binary number with up to 30 digits to a decimal number using a function named `binary_to_decimal`. The function should take a string of binary digits as input and return the corresponding decimal number as an integer.
"""

def binary_to_decimal(binary_str):
    """
    Convert a binary number with up to 30 digits to a decimal number.

    Args:
        binary_str (str): A string of binary digits.

    Returns:
        int: The corresponding decimal number.
    """
    decimal_num = 0
    for i, digit in enumerate(binary_str[::-1]):
        decimal_num += int(digit) * (2 ** i)
    return decimal_num