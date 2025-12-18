"""
QUESTION:
Write a function named `get_index` that takes a list `chars` and an element as input, and returns the index of the element in the list if it exists, otherwise returns a value indicating the element was not found. The function should not use a try/except block and should be optimized for cases where the element is frequently not in the list.
"""

def get_index(chars, element):
    """
    Returns the index of the element in the list if it exists, 
    otherwise returns -1 indicating the element was not found.

    Args:
        chars (list): The list to search in.
        element: The element to search for.

    Returns:
        int: The index of the element if found, -1 otherwise.
    """
    if element in chars:
        return chars.index(element)
    else:
        return -1