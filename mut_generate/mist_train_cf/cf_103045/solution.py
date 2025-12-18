"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the reversed string. The function should not use any built-in string manipulation functions or libraries. The input string is guaranteed to be non-empty.
"""

def reverse_string(s):
    """
    Reverses the input string without using built-in string manipulation functions or libraries.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    reversed_string = ''

    # Iterate over the characters in reverse order
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]

    return reversed_string