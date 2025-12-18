"""
QUESTION:
Write a function `binary_to_decimal(binary)` that converts a given binary number into its decimal equivalent. The function should take a string of binary digits (0s and 1s) as input and return the corresponding decimal number. The input may be a string or integer representation of a binary number.
"""

def binary_to_decimal(binary):
    """
    Converts a given binary number into its decimal equivalent.
    
    Parameters:
    binary (str): A string of binary digits (0s and 1s).
    
    Returns:
    int: The decimal equivalent of the input binary number.
    """
    binary = str(binary)
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal