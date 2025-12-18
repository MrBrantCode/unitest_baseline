"""
QUESTION:
Write a function `octal_to_binary` that takes a string representing an octal number as input and returns the corresponding binary representation as a string. The input string is guaranteed to be a valid octal number.
"""

def octal_to_binary(octal):
    """
    Converts a given octal number to its binary representation.
    
    Parameters:
    octal (str): A string representing a valid octal number.
    
    Returns:
    str: The binary representation of the input octal number as a string.
    """
    decimal = int(octal, 8)
    return bin(decimal)[2:]