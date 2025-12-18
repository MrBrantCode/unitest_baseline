"""
QUESTION:
Create a function called `remove_element` that takes a list and an element as input, and returns the updated list after removing the given element. The function should not use the built-in `remove()` function and should handle cases where the element is not found in the list. The element to be removed will be provided as input from the user.
"""

def remove_element(data_list, element):
    """
    Removes the given element from the list.

    Args:
        data_list (list): The input list.
        element: The element to be removed.

    Returns:
        list: The updated list after removing the element.
    """
    return [x for x in data_list if x != element]