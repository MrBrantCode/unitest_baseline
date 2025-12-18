"""
QUESTION:
Write a function `find_max(arr)` that takes an array of integers as input and returns the maximum number in the array. The function should have a time complexity of O(n log n) and cannot use the built-in `max()` function.
"""

def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])
    
    return max(left_max, right_max)