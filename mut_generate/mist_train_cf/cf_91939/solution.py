"""
QUESTION:
Write a function named `find_minimum` that takes an array as input and returns the minimum value in the array, with a time complexity of O(n log n).
"""

def find_minimum(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return min(arr[0], arr[1])
    
    mid = len(arr) // 2
    left_min = find_minimum(arr[:mid])
    right_min = find_minimum(arr[mid:])
    
    return min(left_min, right_min)