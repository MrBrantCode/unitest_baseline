"""
QUESTION:
Implement a recursive function `is_sorted(arr)` that checks if a given list of integers `arr` is sorted in non-decreasing order without using any built-in sorting functions or loops. The function should return `True` if the list is sorted correctly and `False` otherwise.
"""

def entrance(arr):
    # Base case: an empty list or a list with a single element is always considered sorted
    if len(arr) <= 1:
        return True
    
    # Recursive case: check if the first two elements are in non-decreasing order,
    # and recursively check the rest of the list
    return arr[0] <= arr[1] and entrance(arr[1:])