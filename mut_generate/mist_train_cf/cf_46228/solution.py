"""
QUESTION:
Implement a function named `sort_elements` that takes an iterable and optional parameters `key` and `reverse` to sort the elements of the given iterable in a specific order. The `key` parameter is a function that serves as a basis of sort comparison, and the `reverse` parameter is a boolean that reverses the order of the sorted elements if set to `True`. The function should return the sorted elements.
"""

def sort_elements(iterable, key=None, reverse=False):
    """
    Sorts the elements of the given iterable in a specific order.

    Args:
    iterable: The input iterable to be sorted.
    key (optional): A function that serves as a basis of sort comparison. Defaults to None.
    reverse (optional): A boolean that reverses the order of the sorted elements if set to True. Defaults to False.

    Returns:
    The sorted elements.
    """
    return sorted(iterable, key=key, reverse=reverse)