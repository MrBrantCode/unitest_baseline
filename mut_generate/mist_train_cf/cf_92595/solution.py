"""
QUESTION:
Create a function called `reverse_and_uppercase` that takes a list of strings as input and returns the list with the elements in reverse order and all characters converted to uppercase.
"""

def reverse_and_uppercase(strings):
    """
    This function takes a list of strings, reverses the order of the list, 
    and converts all characters in the strings to uppercase.

    Args:
        strings (list): A list of strings.

    Returns:
        list: The list of strings in reverse order with all characters in uppercase.
    """
    return [item.upper() for item in reversed(strings)]