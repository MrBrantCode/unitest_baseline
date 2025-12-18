"""
QUESTION:
Write a function named `max_depth_of_nested_list` that calculates the maximum depth of a given nested list. The function should take one argument, a list that may contain nested lists of arbitrary depth, and return an integer representing the maximum depth. The function should be able to handle lists of any size and shape, and should be able to handle non-list elements within the list.
"""

def max_depth_of_nested_list(nested_list):
    """
    Calculate the maximum depth of a given nested list.

    Args:
        nested_list (list): A list that may contain nested lists of arbitrary depth.

    Returns:
        int: The maximum depth of the nested list.
    """
    max_depth = 1
    for inner_list in nested_list:
        depth = 1
        if isinstance(inner_list, list):
            depth += max_depth_of_nested_list(inner_list)
        max_depth = max(depth, max_depth)
    return max_depth