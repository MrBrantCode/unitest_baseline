"""
QUESTION:
Write a function `reverse_string_in_place` that takes a string as input and returns the reversed string without using any additional data structures or built-in functions. The input string should be reversed in place, meaning that the original string is modified to be its reverse. Note that strings are immutable in Python, so a conversion to a list of characters may be necessary.
"""

def reverse_string_in_place(s):
    """
    Reverses a string in place without using any additional data structures or built-in functions.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    s = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return ''.join(s)