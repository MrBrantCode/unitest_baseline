"""
QUESTION:
Write a function named `merge_and_sort` that takes two lists of integers as input, combines them into a single list, and returns the combined list in ascending order.
"""

def merge_and_sort(list1, list2):
    """
    This function merges two lists of integers and returns the combined list in ascending order.

    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.

    Returns:
        list: The combined list in ascending order.
    """
    # Combine the two lists into a single list
    combined_list = list1 + list2
    
    # Sort the combined list in ascending order
    sorted_list = sorted(combined_list)
    
    return sorted_list