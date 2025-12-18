"""
QUESTION:
Write a function `reverse_list` that takes a list of alphanumeric characters as input and returns the reversed list. The function should not use the built-in `reverse()` function.
"""

def reverse_list(lst):
    """
    This function takes a list of alphanumeric characters as input and returns the reversed list.
    
    Parameters:
    lst (list): A list of alphanumeric characters.
    
    Returns:
    list: The reversed list.
    """
    return lst[::-1]