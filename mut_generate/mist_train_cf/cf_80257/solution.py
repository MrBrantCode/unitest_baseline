"""
QUESTION:
Write a function named `part_rev` that takes a string `s` as input. Partition `s` into two parts from the middle, reverse the order of the two parts, and then reverse the order of the characters in each part. The string length can be up to 10^6 characters. Optimize the solution for time complexity.
"""

def part_rev(s):
    """
    Partitions the string into two halves from the middle, 
    reverses the order of the two parts and then reverses 
    the order of the characters in each part.

    Args:
        s (str): Input string

    Returns:
        str: Modified string with reversed parts and characters
    """
    l = len(s)
    first_half = s[:l//2][::-1]
    second_half = s[l//2:][::-1]

    return second_half + first_half