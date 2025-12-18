"""
QUESTION:
Write a function that merges two sorted arrays into a single one. The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.
"""

def merge_sorted_arrays(arr1, arr2):
    """
    Merges two sorted arrays of integers into a single sorted array with no duplicates.

    Parameters:
    arr1 (list of int): The first sorted array of integers.
    arr2 (list of int): The second sorted array of integers.

    Returns:
    list of int: A sorted array containing all unique elements from arr1 and arr2.
    """
    return sorted(set(arr1 + arr2))