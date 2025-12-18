"""
QUESTION:
Create a function called `copy_list` that takes a list as input and returns a new list that is a copy of the input list. The new list should not be affected by any modifications to the original list.
"""

def copy_list(input_list):
    """
    Returns a new list that is a copy of the input list.
    
    The new list is not affected by any modifications to the original list.
    
    Args:
        input_list (list): The list to be copied.
    
    Returns:
        list: A new list that is a copy of the input list.
    """
    return input_list[:]  # can also use list(input_list)