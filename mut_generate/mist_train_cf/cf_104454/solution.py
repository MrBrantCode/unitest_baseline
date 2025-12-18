"""
QUESTION:
Create a function `increase_string` that takes a string as input and returns the string with an additional character 'a' appended to the end, but only if the string is not empty. The function should have a time complexity of O(n), where n is the length of the original string.
"""

def increase_string(s):
    """
    Appends a character 'a' to the end of the input string if it's not empty.

    Args:
        s (str): The input string.

    Returns:
        str: The string with an additional character 'a' appended to the end if the string is not empty.
    """
    return s + "a" if s else None