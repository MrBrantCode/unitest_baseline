"""
QUESTION:
Create a function called reverse_list() that takes a list as input and returns the list with its elements in reverse order. The function must not use the built-in reverse() function.
"""

def reverse_list(input_list):
    """
    Reverses the order of elements in a list.

    Args:
        input_list (list): The list to be reversed.

    Returns:
        list: The reversed list.
    """
    return input_list[::-1]