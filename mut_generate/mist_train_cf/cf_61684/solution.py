"""
QUESTION:
Write a function named `find_middle_element` that takes a list of integers as input and returns the middle element. If the list has an odd number of elements, the middle element is at the index equal to the integer division of the list length by 2.
"""

def find_middle_element(lst):
    """
    Returns the middle element of a list of integers.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        int: The middle element of the list.
    """
    return lst[len(lst) // 2]