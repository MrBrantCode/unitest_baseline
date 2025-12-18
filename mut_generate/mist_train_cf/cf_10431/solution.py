"""
QUESTION:
Write a function named `have_common_element` that takes two lists as input and returns `True` if the lists have at least one common element, and `False` otherwise. The function should be able to handle lists containing elements of different data types, such as integers, strings, and booleans.
"""

def have_common_element(list1, list2):
    """
    This function checks if two lists have at least one common element.

    Args:
        list1 (list): The first list to check.
        list2 (list): The second list to check.

    Returns:
        bool: True if the lists have at least one common element, False otherwise.
    """
    for element in list1:
        if element in list2:
            return True
    return False