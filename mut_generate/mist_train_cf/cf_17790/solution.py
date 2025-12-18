"""
QUESTION:
Write a function `find_longest_zeros(binary_string)` that takes a binary string of length up to 10^5 characters as input. The function should return the index of the first zero in the longest consecutive sequence of zeros surrounded by ones. If there are multiple sequences of the same length, return the index of the first occurring sequence.
"""

def find_longest_zeros(binary_string):
    """
    This function finds the index of the first zero in the longest consecutive sequence of zeros 
    surrounded by ones in a binary string.

    Args:
    binary_string (str): A binary string of length up to 10^5 characters.

    Returns:
    int: The index of the first zero in the longest consecutive sequence of zeros.
    """

    longest_zeros = 0
    longest_zeros_start_index = -1
    current_zeros = 0
    current_zeros_start_index = -1

    for i in range(len(binary_string)):
        if binary_string[i] == '1':
            if current_zeros > longest_zeros:
                longest_zeros = current_zeros
                longest_zeros_start_index = current_zeros_start_index
            current_zeros = 0
            current_zeros_start_index = -1
        elif binary_string[i] == '0':
            if current_zeros_start_index == -1:
                current_zeros_start_index = i
            current_zeros += 1

    if current_zeros > longest_zeros:
        longest_zeros = current_zeros
        longest_zeros_start_index = current_zeros_start_index

    return longest_zeros_start_index