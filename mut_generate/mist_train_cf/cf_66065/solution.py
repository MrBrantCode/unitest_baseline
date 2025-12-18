"""
QUESTION:
Implement a function `union_and_intersection(list1, list2)` that compares two sorted lists and returns a new sorted list containing the intersection of these two lists and the union of these two lists. The intersection list should first display the common elements between the two lists, then followed by the unique elements from both lists sorted in ascending order. The implementation must not use Python's built-in intersection (&) and union (|) operators.
"""

def union_and_intersection(list1, list2):
    """
    This function compares two sorted lists and returns a new sorted list containing 
    the intersection of these two lists and the union of these two lists.

    Args:
    list1 (list): The first sorted list.
    list2 (list): The second sorted list.

    Returns:
    tuple: A tuple containing the intersection and union of the input lists.
    """
    intersection = [value for value in list1 if value in list2]
    union = sorted(list(set(list1 + list2)))

    return intersection, union