"""
QUESTION:
Create a function called `reverse_string` that takes one argument `input_string`. The function should return the input string reversed. The reversed string should handle all types of characters including letters, digits, special characters, and Unicode characters consisting of two or more code units.
"""

def reverse_string(input_string):
    """
    Reverses the input string while handling all types of characters including 
    letters, digits, special characters, and Unicode characters consisting of 
    two or more code units.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    reversed_string = input_string[::-1]
    return reversed_string