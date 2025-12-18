"""
QUESTION:
Write a function `find_min_diff(A, M)` that finds the minimum absolute difference between any two elements at odd indices in the array `A` that is greater than `M`. The function should have a time complexity of O(n log n) or better, where n is the number of elements in `A`.
"""

def find_min_diff(A, M):
    """
    This function finds the minimum absolute difference between any two elements 
    at odd indices in the array A that is greater than M.

    Args:
        A (list): An integer array.
        M (int): The minimum difference value.

    Returns:
        int: The minimum absolute difference greater than M, or -1 if no such pair exists.
    """
    odd_items = [A[i] for i in range(len(A)) if i % 2 != 0] # extract the elements of odd indices
    odd_items.sort() # sort the odd-indexed elements

    min_diff = float('inf') # initialize min_difference with a large number

    for i in range(1, len(odd_items)): 
        diff = abs(odd_items[i] - odd_items[i-1]) # find the absolute difference
        if diff > M and diff < min_diff: # check the constraints 
            min_diff = diff # update the min_diff 

    return min_diff if min_diff != float('inf') else -1