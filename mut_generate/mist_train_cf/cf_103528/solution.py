"""
QUESTION:
Write a function `flatten_list` that takes a list of lists as input and returns a new list containing all the elements from the sub-lists. The function should handle a list with any number of sub-lists, and each sub-list can contain any number of elements.
"""

def flatten_list(lst):
    """
    This function takes a list of lists as input and returns a new list containing all the elements from the sub-lists.

    Args:
        lst (list): A list of lists.

    Returns:
        list: A new list containing all the elements from the sub-lists.
    """
    return [x for i in lst for x in i]