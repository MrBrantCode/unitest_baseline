"""
QUESTION:
Design a function named `max_zeros` that takes two non-negative integers `start` and `end` as input where `start` is less than or equal to `end`. The function should calculate the total number of zeros in all binary representations of numbers between `start` and `end` inclusive, and find the binary number with the maximum number of zeros within the given range.
"""

def max_zeros(start, end):
    """
    Calculate the total number of zeros in all binary representations of numbers 
    between start and end inclusive, and find the binary number with the maximum 
    number of zeros within the given range.

    Args:
    start (int): The start of the range (inclusive).
    end (int): The end of the range (inclusive).

    Returns:
    tuple: A tuple containing the maximum number of zeros and the binary number 
           with the maximum number of zeros.
    """
    max_zeros = -1
    max_binary = 0
    for i in range(start, end+1):
        binary = bin(i)[2:]  # remove '0b' prefix
        num_zeros = binary.count('0')
        if num_zeros > max_zeros:
            max_zeros = num_zeros
            max_binary = binary
    return max_zeros, max_binary