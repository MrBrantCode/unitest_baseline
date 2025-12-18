"""
QUESTION:
Write a function called `find_all_indices` that takes a list and a target element as input and returns a list of all indices where the target element appears in the list.
"""

def find_all_indices(lst, target):
    """
    Returns a list of all indices where the target element appears in the list.
    
    Args:
        lst (list): The list to search in.
        target: The target element to search for.
    
    Returns:
        list: A list of indices where the target element appears.
    """
    return [i for i, x in enumerate(lst) if x == target]