"""
QUESTION:
Given an array of integers and a positive integer K, return a subset of exactly K elements with the maximum possible sum. The function should take two parameters: the array and the size of the subset. The function must return a subset of the original array.
"""

def entrance(arr, K):
    """
    Returns a subset of size K with the maximum possible sum from the given array.

    Args:
    arr (list): The input array of integers.
    K (int): The size of the subset.

    Returns:
    list: A subset of the original array with the maximum possible sum.
    """
    return sorted(arr, reverse=True)[:K]