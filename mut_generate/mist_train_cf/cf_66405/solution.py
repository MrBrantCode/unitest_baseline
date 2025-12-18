"""
QUESTION:
Construct a boolean function named "is_num_even_in_binary" that accepts an integer input and returns True if the least significant bit in its binary representation is 0, indicating the number is even in binary. The function should only consider the binary representation to determine evenness, not the decimal representation.
"""

def is_num_even_in_binary(num):
    """
    Checks if the least significant bit in the binary representation of a number is 0.
    
    Args:
        num (int): The input number.
    
    Returns:
        bool: True if the number is even in binary, False otherwise.
    """
    binary_num = bin(num)[2:] # Convert to binary and remove '0b' at the start
    return binary_num[-1] == '0'