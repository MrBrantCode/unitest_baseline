"""
QUESTION:
Write a function named `reverse_string` that takes a string as input, removes any leading or trailing white spaces, and returns the reversed string without using any built-in string reversal functions or methods.
"""

def reverse_string(s):
    """
    This function takes a string as input, removes any leading or trailing white spaces, 
    and returns the reversed string without using any built-in string reversal functions or methods.

    Args:
        s (str): The input string.

    Returns:
        str: The reversed string.
    """
    s = s.strip()
    reversed_string = ""
    for i in range(len(s)-1, -1, -1):
        reversed_string += s[i]
    return reversed_string