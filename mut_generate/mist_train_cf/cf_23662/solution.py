"""
QUESTION:
Create a function `sort_array` that takes an array of integers as input and returns the array sorted in ascending order. The function should not use any pre-defined sorting functions. The input array may contain duplicate values and its length can vary. The function should be efficient and have a minimum time complexity of O(n^2).
"""

def sort_array(A):
    """
    Sorts an array of integers in ascending order without using any pre-defined sorting functions.
    
    Parameters:
    A (list): The input array of integers.
    
    Returns:
    list: The sorted array in ascending order.
    """
    n = len(A)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True
        if not swapped:
            break
    return A