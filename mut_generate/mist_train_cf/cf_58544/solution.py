"""
QUESTION:
Write a function `flatten_nested_list(nested_list)` that takes a nested list of varying depth as input, and returns a new list with all elements flattened and sorted in ascending order, excluding non-integer elements. The function should be optimized for large lists.
"""

def entrance(nested_list):
    """
    This function takes a nested list of varying depth as input, 
    and returns a new list with all elements flattened and sorted in ascending order, 
    excluding non-integer elements.

    Args:
        nested_list (list): A list of varying depth containing integers and/or other lists.

    Returns:
        list: A new list with all elements flattened and sorted in ascending order.
    """
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(entrance(i))
        else:
            if isinstance(i, int):
                flat_list.append(i)
    return sorted(flat_list)