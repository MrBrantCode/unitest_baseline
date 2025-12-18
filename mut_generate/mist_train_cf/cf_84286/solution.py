"""
QUESTION:
Write a Python function named `reverse_and_sort` that takes two parameters: an array `arr` and a position `pos`. The function should reverse the elements in the array up to the given position and sort the remaining elements in ascending order. If the array is empty, the function should return an empty array. If the position is out of the array's bounds, the function should reverse the entire array. If the array has only one element, the function should return the original array.
"""

def reverse_and_sort(arr, pos):
    if not arr:   # if array is empty
        return []
    if pos >= len(arr):   # if position is out of array's bounds
        return list(reversed(arr))
    if len(arr) == 1:   # if array only has one element
        return arr
        
    # reverse part of the array and sort the remaining part
    return list(reversed(arr[:pos])) + sorted(arr[pos:])