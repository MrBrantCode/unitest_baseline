"""
QUESTION:
Write a function `find_min` that takes a tuple of n elements as input, where all elements are positive integers. The function must return the minimum value from the tuple in O(n) time complexity without using any built-in Python functions or libraries for sorting or finding the minimum value.
"""

def find_min(lst):
    """
    This function finds the minimum value from a tuple of positive integers in O(n) time complexity.
    
    Parameters:
    lst (tuple): A tuple of positive integers.
    
    Returns:
    int: The minimum value from the tuple.
    """
    min_val = lst[0] # Initialize the min_val with the first element of the tuple
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val