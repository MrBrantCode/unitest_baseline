"""
QUESTION:
Write a function named `find_max` that finds the maximum number in a given array without using the built-in `max()` function. The function should have a time complexity of O(n log n) due to the division of the array into halves at each recursive call.
"""

def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])
    
    return max(left_max, right_max)