"""
QUESTION:
Implement a function named `is_sorted` that takes a list of integers as input and returns True if the list is sorted in non-decreasing order, and False otherwise. The function should be recursive and handle edge cases such as an empty list and a list with duplicate elements. The implementation should not use any built-in sorting functions or loops.
"""

def is_sorted(arr):
    # Base case: an empty list or a list with a single element is always considered sorted
    if len(arr) <= 1:
        return True
    
    # Recursive case: check if the first two elements are in non-decreasing order,
    # and recursively check the rest of the list
    return arr[0] <= arr[1] and is_sorted(arr[1:])