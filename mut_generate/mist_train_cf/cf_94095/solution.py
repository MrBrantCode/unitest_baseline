"""
QUESTION:
Write a function named `get_unique_elements` that takes in a list of elements (can be integers, strings, or floats) and returns a new list containing only the unique elements from the original list while preserving their order. The function should also modify the original list to only contain the unique elements. Implement an efficient solution using a set to handle large lists with millions of elements without running out of memory or causing a significant delay in execution.
"""

def get_unique_elements(lst):
    """
    Returns a new list containing only the unique elements from the original list 
    while preserving their order. The function also modifies the original list to 
    only contain the unique elements.

    Args:
        lst (list): A list of elements (can be integers, strings, or floats)

    Returns:
        list: A new list containing only the unique elements from the original list
    """
    unique_set = set()
    unique_list = []
    for elem in lst:
        if elem not in unique_set:
            unique_set.add(elem)
            unique_list.append(elem)
    lst.clear()
    lst.extend(unique_list)
    return unique_list