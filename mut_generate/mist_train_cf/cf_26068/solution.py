"""
QUESTION:
Given a sorted array of size n, write a function `findKthSmallestElement(arr, n, k)` that returns the kth smallest element. The array is 0-indexed, and k is 1-indexed, meaning the first element is considered the 1st smallest element. The function should not perform any sorting operations as the input array is already sorted.
"""

def findKthSmallestElement(arr, n, k): 
    """
    Returns the kth smallest element in a sorted array.

    Args:
        arr (list): A sorted list of elements.
        n (int): The size of the array.
        k (int): The index of the desired element (1-indexed).

    Returns:
        The kth smallest element in the array.
    """
    return arr[k-1]