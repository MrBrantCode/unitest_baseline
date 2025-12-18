"""
QUESTION:
Write a function called `linear_search` that finds an element in a list and determine its time complexity in Big O notation. The function should take two parameters: a list of elements and the target element to search for.
"""

def linear_search(lst, target):
    """
    This function performs a linear search on a given list to find a target element.
    
    Parameters:
    lst (list): The list of elements to search through.
    target: The element to search for.
    
    Returns:
    int: The index of the target element if found, -1 otherwise.
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1