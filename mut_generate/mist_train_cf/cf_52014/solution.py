"""
QUESTION:
Write a function named `flatten_list` that takes a 2D matrix as input and returns a single linear list while preserving the original order. The function must use recursion and cannot use any built-in Python functions.
"""

def entance(nested_list):
    if not nested_list:
        return []

    first_list, remaining_lists = nested_list[0], nested_list[1:]

    flat_list = []
    for element in first_list:
        flat_list.append(element)

    return flat_list + entance(remaining_lists)