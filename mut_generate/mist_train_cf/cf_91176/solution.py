"""
QUESTION:
Remove Duplicates and Sort Array Function: unique_elements
Create a function named 'unique_elements' that takes a list of integers as input, removes duplicates, and returns the list in ascending order. The function should not use any additional space that scales with input size.
"""

def unique_elements(arr):
    """
    This function takes a list of integers as input, removes duplicates, and returns the list in ascending order.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    list: A list of unique integers in ascending order.
    """
    unique_arr = list(set(arr))
    unique_arr.sort()
    return unique_arr