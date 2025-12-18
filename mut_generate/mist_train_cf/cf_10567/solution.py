"""
QUESTION:
Create a function called `delete_element` that takes a list `lst` and an `element` as parameters. The function should delete all occurrences of the given `element` from the `lst` and return `True` if the `element` was found in the list, and `False` otherwise.
"""

def delete_element(lst, element):
    """
    Deletes all occurrences of the given element from the list.

    Args:
        lst (list): The list to remove elements from.
        element: The element to remove.

    Returns:
        bool: True if the element was found in the list, False otherwise.
    """
    found = False
    while element in lst:
        lst.remove(element)
        found = True
    return found