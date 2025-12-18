"""
QUESTION:
Implement a function `reverse_string` that takes a list of characters as input, reverses the order of the characters without using any built-in reverse functions, and returns the reversed string in uppercase.
"""

def reverse_string(s):
    """
    Reverses the order of characters in a list and returns the result in uppercase.

    Args:
        s (list): A list of characters.

    Returns:
        str: The reversed string in uppercase.
    """
    stack = []
    for char in s:
        stack.append(char)
    
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()

    return reversed_str.upper()