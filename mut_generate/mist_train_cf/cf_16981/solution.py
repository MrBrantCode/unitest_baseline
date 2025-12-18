"""
QUESTION:
Write a function `reverse_string` that takes a null-terminated input string as an argument and returns the reversed string. The function should have a time complexity of O(n), where n is the length of the input string, and it should not use any built-in string manipulation functions. The input string can be up to 10^7 characters long and the function should only use basic data types like integers and characters.
"""

def reverse_string(s):
    """
    Reverses a null-terminated input string.

    Args:
    s (str): The input string to be reversed.

    Returns:
    str: The reversed string.
    """
    
    # Initialize variables
    string_length = 0
    reversed_string = ""

    # Find the length of the input string
    while s[string_length] != '\0':
        string_length += 1

    # Reverse the string by iterating from the end to the beginning
    index = string_length - 1
    while index >= 0:
        reversed_string += s[index]
        index -= 1

    return reversed_string