"""
QUESTION:
Write a function `limit_list_length` that takes a list as input and returns the list with at most 100 elements by removing the oldest elements.
"""

def limit_list_length(input_list):
    """
    This function limits the length of the input list to 100 elements.
    If the list has more than 100 elements, it removes the oldest elements.
    
    Args:
        input_list (list): The list to be limited in length.
    
    Returns:
        list: The list with at most 100 elements.
    """
    if len(input_list) > 100:
        return input_list[-100:]
    return input_list