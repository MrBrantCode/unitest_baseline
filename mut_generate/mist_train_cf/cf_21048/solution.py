"""
QUESTION:
Write a function called `reverse_string` that takes an alphanumeric string as input, reverses it using recursion, and returns the reversed string. The input string has a maximum length of 100 characters and the solution should have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(string):
    """
    Reverses an alphanumeric string using recursion.

    Args:
        string (str): The input alphanumeric string.

    Returns:
        str: The reversed string.
    """
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]