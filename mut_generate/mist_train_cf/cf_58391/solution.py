"""
QUESTION:
Write a function called `rotate` that takes an integer `n` as input and performs a bitwise left rotation operation on it, handling the case when the input is greater than 127. The function should return the rotated integer, ensuring the result is within the range of an 8-bit unsigned integer (0 to 255).
"""

def rotate(n):
    """
    Performs a bitwise left rotation operation on the given integer n.
    
    If the input is greater than 127, it handles the case by taking the modulus of n with 256 (the maximum value for an 8-bit unsigned integer + 1) 
    to ensure the result is within the range of an 8-bit unsigned integer (0 to 255).

    Args:
        n (int): The input integer to be rotated.

    Returns:
        int: The rotated integer.
    """
    return (n << 1) % 256