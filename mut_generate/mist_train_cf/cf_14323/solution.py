"""
QUESTION:
Create a function called `doubled_sorted_list` that takes a list of integers as input, doubles each element, sorts the resulting list in ascending order, and returns the new list without modifying the original list.
"""

def doubled_sorted_list(lst):
    """
    This function takes a list of integers, doubles each element, sorts the resulting list in ascending order, 
    and returns the new list without modifying the original list.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        list: A new sorted list where each element is double the value of the corresponding element in the input list.
    """
    return sorted([2 * x for x in lst])