"""
QUESTION:
Implement a function `reverse_string` that takes a string `input_str` as input and returns a new string that is the reverse of the input string. The function should not use any built-in functions or methods that directly reverse a string, handle special characters and whitespace, and preserve the original case of each character in the reversed string. The function should work correctly for strings containing uppercase and lowercase letters, special characters, and whitespace.
"""

def reverse_string(input_str):
    """
    Reverses the input string while preserving the original case of each character.

    Args:
        input_str (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    reversed_str = ''
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str