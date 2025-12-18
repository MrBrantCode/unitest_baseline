"""
QUESTION:
Write a function `common_elements` that takes two lists as input and returns a list of their common elements, with no duplicates, in ascending order. The function should have a time complexity of O(n) and only use the built-in functions `len()`, `range()`, and `int()`.
"""

def common_elements(list1, list2):
    """
    Returns a list of common elements between two lists, with no duplicates, in ascending order.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A list of common elements.
    """
    common_elements = []
    list1_set = set(list1)
    list2_set = set(list2)

    for num in list1_set:
        if num in list2_set:
            common_elements.append(num)

    return sorted(set(common_elements))