"""
QUESTION:
Write a function `binary_to_decimal` that takes a binary number as a string input and returns its decimal equivalent.
"""

def binary_to_decimal(binary_str):
    """
    This function converts a binary number represented as a string into its decimal equivalent.

    Args:
        binary_str (str): A binary number as a string.

    Returns:
        int: The decimal equivalent of the binary number.
    """
    return int(binary_str, 2)