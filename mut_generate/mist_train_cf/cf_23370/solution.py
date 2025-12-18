"""
QUESTION:
Write a function `merge_lists` that takes two lists as input and returns a new list containing all elements from both lists. The input lists contain only integers. The function should not modify the original lists. The order of elements in the resulting list should be the same as in the input lists.
"""

def merge_lists(list1, list2):
    """
    This function merges two lists of integers into a new list.
    
    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.
    
    Returns:
        list: A new list containing all elements from both input lists.
    """
    return list1 + list2