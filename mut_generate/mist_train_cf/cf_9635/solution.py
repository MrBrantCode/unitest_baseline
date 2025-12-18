"""
QUESTION:
Write a function `kth_smallest_element(lst, k)` that retrieves the kth smallest element from a given list `lst`, where `k` is an integer greater than or equal to 1. The function should assume that `k` is valid and that `lst` contains at least `k` elements.
"""

def entrance(lst, k):
    lst.sort()  # Sort the list in ascending order
    return lst[k-1]  # Return the kth smallest element (at index k-1)