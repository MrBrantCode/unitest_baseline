"""
QUESTION:
Write a function called `reverse_list` that takes a list as input and returns the elements of the list in the opposite order of their initial arrangement without using the built-in `reverse()` function.
"""

def reverse_list(input_list):
    """
    Returns the elements of the input list in the opposite order of their initial arrangement.
    
    Args:
        input_list (list): The list to be reversed.
    
    Returns:
        list: The reversed list.
    """
    return input_list[::-1]