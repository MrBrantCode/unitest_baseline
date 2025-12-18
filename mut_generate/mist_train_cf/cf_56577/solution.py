"""
QUESTION:
Find the index of a unique element in a list using Python. The list and the target element will be provided. The solution should be implemented in a function named `find_index`. The list is not guaranteed to contain the target element. The solution must handle this scenario. The time complexity of the solution should be considered.
"""

def find_index(lst, target):
    """
    This function finds the index of a unique element in a list.
    
    Parameters:
    lst (list): The list to search in.
    target: The target element to search for.
    
    Returns:
    int: The index of the target element if found, -1 otherwise.
    """
    try:
        return lst.index(target)
    except ValueError:
        return -1