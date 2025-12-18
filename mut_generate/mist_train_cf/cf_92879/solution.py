"""
QUESTION:
Write a function `binary_to_int` that takes a binary string as input and returns its equivalent integer value. The function should not use any built-in functions or libraries to perform the conversion. The input string only contains the characters '0' and '1'.
"""

def binary_to_int(binary_string):
    """
    This function converts a binary string into its equivalent integer value.
    
    Parameters:
    binary_string (str): A string of binary digits ('0' or '1').
    
    Returns:
    int: The integer equivalent of the binary string.
    """
    result = 0
    for bit in binary_string:
        result = result * 2 + (ord(bit) - ord('0'))
    return result