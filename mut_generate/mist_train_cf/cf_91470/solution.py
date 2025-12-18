"""
QUESTION:
Combine two lists into a single sorted list in ascending order.

Create a function `combine_and_sort` that takes two lists as input, combines them into a single list, and returns the combined list sorted in ascending order. The input lists may contain duplicate elements.
"""

def combine_and_sort(list_first, list_second):
    """
    Combine two lists into a single sorted list in ascending order.

    Args:
        list_first (list): The first list to combine.
        list_second (list): The second list to combine.

    Returns:
        list: The combined list sorted in ascending order.
    """
    combined_list = list_first + list_second
    return sorted(combined_list)