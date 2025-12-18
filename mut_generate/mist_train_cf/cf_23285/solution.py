"""
QUESTION:
Write a function named `binary_to_decimal` to convert a binary number to a decimal number. The function should take a binary number as input and return its decimal equivalent. The binary number is a string of '0's and '1's, and the function should not assume any maximum length for the input.
"""

def binary_to_decimal(binary_number):
    """
    Converts a binary number to a decimal number.

    Args:
    binary_number (str): A string of '0's and '1's representing the binary number.

    Returns:
    int: The decimal equivalent of the binary number.
    """
    return int(binary_number, 2)