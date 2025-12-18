"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the string with its characters in reverse order. Implement this using nested loops and without using any built-in string manipulation functions or methods. The solution should achieve a time complexity of O(n).
"""

def reverse_string(s):
    """
    This function takes a string as input and returns the string with its characters in reverse order.

    Args:
    s (str): The input string.

    Returns:
    str: The reversed string.
    """
    return ''.join([char for char in s[::-1]])