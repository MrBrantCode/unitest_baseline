"""
QUESTION:
Create a function `unique_elements()` that takes a list as input and returns a set containing all unique elements from the list, with no duplicates. The order of elements in the output set is not important.
"""

def unique_elements(input_list):
    """
    Returns a set containing all unique elements from the input list.

    Args:
        input_list (list): The input list that may contain duplicate elements.

    Returns:
        set: A set containing all unique elements from the input list.
    """
    return set(input_list)