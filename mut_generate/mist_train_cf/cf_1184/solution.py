"""
QUESTION:
Write a function called decimal_to_binary that takes an integer as input and returns its binary representation as a string. The binary representation should not exceed 8 digits and the function should run in O(log n) time complexity, where n is the input number.
"""

def decimal_to_binary(n):
    """
    This function converts a decimal number to its binary representation as a string.
    
    Parameters:
    n (int): The decimal number to be converted.
    
    Returns:
    str: The binary representation of the decimal number as a string.
    """
    binary = ""
    while n > 0 and len(binary) <= 8:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary