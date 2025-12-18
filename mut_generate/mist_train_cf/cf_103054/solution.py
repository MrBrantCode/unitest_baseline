"""
QUESTION:
Write a function to remove all duplicate elements from an array and sort it in ascending order.
"""

def remove_duplicates_and_sort(arr):
    """
    Removes all duplicate elements from an array and sorts it in ascending order.

    Args:
        arr (list): The input array.

    Returns:
        list: The array without duplicates, sorted in ascending order.
    """
    return sorted(set(arr))