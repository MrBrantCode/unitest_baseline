"""
QUESTION:
Write a function `count_lowercase` to calculate the total number of lowercase characters in a given string. The function should return the count as an integer.
"""

def count_lowercase(s):
    """
    Calculate the total number of lowercase characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The total count of lowercase characters.
    """
    total = 0
    for char in s:
        if char.islower():
            total += 1
    return total