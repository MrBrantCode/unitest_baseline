"""
QUESTION:
Create a function called `reverse_string` that takes one string argument and returns the reversed string. The function should not use any built-in string reversal methods, and the input string may contain any characters including spaces and punctuation.
"""

def reverse_string(input_str):
    """
    Reverses a given string without using built-in string reversal methods.

    Args:
        input_str (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    reversed_str = ""
    for i in range(len(input_str) - 1, -1, -1):
        reversed_str += input_str[i]
    return reversed_str