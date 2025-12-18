"""
QUESTION:
Implement the `find_equal_value_pair()` function to find the first pair of alphanumeric strings in a given set whose sum of ASCII values are equal. The function takes in a set of strings as an argument and returns a tuple with the first pair of strings found. The function should be optimized for efficiency. The input set of strings is guaranteed to be non-empty, but may not necessarily contain a pair of strings with equal sum of ASCII values, in which case the function should return `None`.
"""

def find_equal_value_pair(strings):
    """
    Find the first pair of alphanumeric strings in a given set whose sum of ASCII values are equal.

    Args:
    strings (set): A set of alphanumeric strings.

    Returns:
    tuple: A tuple with the first pair of strings found, or None if no pair is found.
    """
    ascii_sum = {}
    for string in strings:
        total = 0
        for char in string:
            total += ord(char)
        if total in ascii_sum:
            return (ascii_sum[total], string)
        ascii_sum[total] = string
    return None