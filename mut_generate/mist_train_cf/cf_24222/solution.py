"""
QUESTION:
Write a function `longestSequenceOfZeros` that takes a string of binary digits as input and returns the length of the longest consecutive sequence of zeros in the string.
"""

def longestSequenceOfZeros(s):
    """
    This function takes a string of binary digits as input and returns the length of the longest consecutive sequence of zeros in the string.

    Parameters:
    s (str): A string of binary digits.

    Returns:
    int: The length of the longest consecutive sequence of zeros in the string.
    """
    max_len = 0
    count = 0
    for char in s:
        if char == '0':
            count += 1
            max_len = max(max_len, count)
        else:
            count = 0
    return max_len