"""
QUESTION:
Write a function `sort_multidimensional_list` that takes a multidimensional list as input and returns a new list sorted in ascending order based on the third element of each sub-list. The function should use a lambda function as the key for sorting and assume that all sub-lists have at least three elements and that the third elements are comparable. If a sub-list lacks a third element or the elements are non-comparable types, the function should raise an error.
"""

def sort_multidimensional_list(input_list):
    """
    Sorts a multidimensional list in ascending order based on the third element of each sub-list.

    Args:
        input_list (list): A list of lists with at least three elements in each sub-list.

    Returns:
        list: A new sorted list.

    Raises:
        IndexError: If any sub-list lacks a third element.
        TypeError: If the third elements are non-comparable types.
    """
    return sorted(input_list, key=lambda x: x[2])