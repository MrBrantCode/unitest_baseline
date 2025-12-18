"""
QUESTION:
The __Hamming weight__ of a string is the number of symbols that are different from the zero-symbol of the alphabet used. There are several algorithms for efficient computing of the Hamming weight for numbers. In this Kata, speaking technically, you have to find out the number of '1' bits in a binary representation of a number. Thus,

The interesting part of this task is that you have to do it *without* string operation (hey, it's not really interesting otherwise)

 ;)
"""

def calculate_hamming_weight(x: int) -> int:
    """
    Calculate the Hamming weight of an integer, which is the number of '1' bits in its binary representation.

    Parameters:
    x (int): The integer whose Hamming weight is to be calculated.

    Returns:
    int: The Hamming weight of the integer.
    """
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count