"""
QUESTION:
Implement the function 'count_bits' that takes an integer as input and returns the number of bits required to represent the integer in binary. The function should be able to handle both positive and negative integers.
"""

def count_bits(n):
    """
    This function takes an integer as input and returns the number of bits required to represent the integer in binary.
    
    Parameters:
    n (int): The input integer.
    
    Returns:
    int: The number of bits required to represent the integer in binary.
    """
    if n == 0:
        return 1
    return n.bit_length()