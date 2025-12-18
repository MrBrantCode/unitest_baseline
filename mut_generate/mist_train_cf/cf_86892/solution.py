"""
QUESTION:
Implement a function called `replace_x_with_y` that takes a string as input and returns the string with all occurrences of 'x' replaced with 'y' without using any built-in string manipulation functions or regular expressions. The function should have a time complexity of O(n) and use only constant space.
"""

def replace_x_with_y(input_string):
    """
    Replaces all occurrences of 'x' with 'y' in the given string.

    Args:
        input_string (str): The input string to replace 'x' with 'y'.

    Returns:
        str: The modified string with all 'x' replaced with 'y'.
    """
    new_string = ""
    for char in input_string:
        if char == 'x':
            new_string += 'y'
        else:
            new_string += char
    return new_string