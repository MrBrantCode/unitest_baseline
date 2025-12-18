"""
QUESTION:
Write a function `longest_zeros(bin_str)` that takes a binary string `bin_str` as input and returns the length of the longest consecutive sequence of zeros and its starting position. The function should handle binary strings of arbitrary length and have a time complexity better than O(n^2). If no sequence of zeros is found, the function should indicate this. The position is 0-indexed.
"""

def longest_zeros(bin_str):
    """
    This function takes a binary string as input and returns the length of the longest 
    consecutive sequence of zeros and its starting position.

    Args:
        bin_str (str): A binary string.

    Returns:
        tuple: A tuple containing the length of the longest sequence of zeros and its starting position.
    """
    max_count = 0
    count = 0
    position = -1
    for i in range(len(bin_str)):
        if bin_str[i] == '0':
            if count == 0:
                temp_position = i
            count += 1
            if count > max_count:
                max_count = count
                position = temp_position
        else:
            count = 0
    if max_count == 0:
        return "No zero sequence found"
    else:
        return max_count, position