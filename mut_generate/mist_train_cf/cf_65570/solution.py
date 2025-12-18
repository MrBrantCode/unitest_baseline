"""
QUESTION:
Write a function named 'reverse_list' that takes a list as input and returns the reversed list. Consider both memory usage and return type when deciding on the implementation, taking into account the trade-offs between using list slicing notation and the built-in reversed() function.
"""

def reverse_list(input_list):
    """
    Returns the reversed input list.
    
    This function uses list slicing to create a new list containing all elements of the original list in the reversed order.
    
    Args:
        input_list (list): The list to be reversed.
    
    Returns:
        list: A new list containing all elements of the original list in the reversed order.
    """
    return input_list[::-1]