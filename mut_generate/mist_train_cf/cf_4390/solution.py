"""
QUESTION:
Write a function called `reverse_string` that takes a string as input and returns the reversed string. The function should not use any built-in functions or methods that directly reverse the string, such as `reversed()` or `string[::-1]`. The function should handle strings of any length and content.
"""

def reverse_string(string):
    """
    Reverses a given string without using built-in reverse functions.

    Args:
    string (str): The input string to be reversed.

    Returns:
    str: The reversed string.
    """
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string