"""
QUESTION:
Write a function `xor_binary` that takes two binary numbers as strings, performs the XOR operation on them, and returns the binary representation of the result as a string. The input binary numbers are represented as strings of 0s and 1s.
"""

def xor_binary(a, b):
    """
    This function takes two binary numbers as strings, performs the XOR operation on them, 
    and returns the binary representation of the result as a string.

    Args:
    a (str): The first binary number as a string.
    b (str): The second binary number as a string.

    Returns:
    str: The binary representation of the XOR result as a string.
    """
    # Convert binary numbers to integers, perform XOR, and convert the result back to binary
    return bin(int(a, 2) ^ int(b, 2))[2:]