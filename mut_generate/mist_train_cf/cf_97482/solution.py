"""
QUESTION:
Write a function `delete_element` that takes two parameters: a list of elements `arr` and a target element `element`. The function should return a new list with all occurrences of `element` removed from `arr`, while maintaining the relative order of the remaining elements.
"""

def delete_element(arr, element):
    """
    Deletes all occurrences of a target element from a list while maintaining the relative order of the remaining elements.

    Args:
        arr (list): The input list of elements.
        element: The target element to be deleted.

    Returns:
        list: A new list with all occurrences of the target element removed.
    """
    return [i for i in arr if i != element]