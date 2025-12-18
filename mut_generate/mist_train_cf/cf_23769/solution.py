"""
QUESTION:
Write a function `binary_to_decimal` that takes a string of binary digits as input and returns the equivalent decimal number. The input string will only contain the characters '0' and '1'.
"""

def binary_to_decimal(binary):
    """
    This function converts a binary number represented as a string into its decimal equivalent.
    
    Parameters:
    binary (str): A string of binary digits.
    
    Returns:
    int: The decimal equivalent of the input binary number.
    """
    return int(binary, 2)