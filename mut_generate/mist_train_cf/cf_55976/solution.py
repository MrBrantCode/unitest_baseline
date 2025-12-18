"""
QUESTION:
Write a function called `mirror_string` that takes a string of characters as input and returns the reverse of the input string. The input string can contain both letters and numbers. The function should not transform letters between uppercase and lowercase.
"""

def mirror_string(s):
    """
    Returns the reverse of the input string.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    return s[::-1]