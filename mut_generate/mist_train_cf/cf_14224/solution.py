"""
QUESTION:
Create a function called `reverse_string` that takes an input string as a parameter and returns the reversed string without using any built-in string reversal functions or methods. The input string can contain any printable ASCII characters. The function should not modify the original input string.
"""

def reverse_string(input_string):
    """
    Reverses the input string without using built-in string reversal functions or methods.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    reversed_string = ""
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string