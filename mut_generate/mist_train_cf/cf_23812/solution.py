"""
QUESTION:
Write a function `remove_duplicates` that takes a list as input and returns a new list containing the unique elements from the original list, in any order, without modifying the original list.
"""

def remove_duplicates(my_list):
    """
    Returns a new list containing the unique elements from the original list, 
    in any order, without modifying the original list.

    Args:
        my_list (list): The input list.

    Returns:
        list: A new list containing the unique elements.
    """
    return list(set(my_list))