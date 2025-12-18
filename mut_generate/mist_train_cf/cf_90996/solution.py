"""
QUESTION:
Write a function named `kth_smallest_element` that takes a list of integers `lst` and an integer `k` as input, where `k` is greater than or equal to 1. The function should return the kth smallest element from the list. The function should handle the 0-based indexing of lists, meaning it should return the element at index `k-1`.
"""

def kth_smallest_element(lst, k):
    lst.sort()  # Sort the list in ascending order
    return lst[k-1]  # Return the kth smallest element (at index k-1)