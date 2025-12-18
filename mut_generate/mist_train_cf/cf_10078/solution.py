"""
QUESTION:
Implement a function `quicksort` that takes a list of integers as input and returns the sorted list in ascending order. The function should use the quicksort algorithm, which works by selecting a pivot element and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays should then be recursively sorted using the same process until the entire list is sorted.
"""

def quicksort(arr):
    """
    This function implements the quicksort algorithm to sort a list of integers in ascending order.
    
    Parameters:
    arr (list): The list of integers to be sorted.
    
    Returns:
    list: The sorted list of integers in ascending order.
    """

    # Base case: If the array has 1 or 0 elements, it is already sorted.
    if len(arr) <= 1:
        return arr
    
    # Choose the rightmost element as the pivot.
    pivot = arr[-1]
    
    # Initialize three lists to store elements less than, equal to, and greater than the pivot.
    left = [x for x in arr[:-1] if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursively sort the sub-arrays and combine the results.
    return quicksort(left) + middle + quicksort(right)