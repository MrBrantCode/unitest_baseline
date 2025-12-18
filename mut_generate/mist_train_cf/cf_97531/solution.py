"""
QUESTION:
Write a function `binary_representation` that converts a given decimal number into its binary representation as a string. The function should take an integer as input and return a string containing the binary representation, excluding the '0b' prefix.
"""

def binary_representation(n):
    """
    Converts a given decimal number into its binary representation as a string.
    
    Args:
        n (int): The decimal number to be converted.
    
    Returns:
        str: The binary representation of the decimal number as a string.
    """
    return bin(n)[2:]