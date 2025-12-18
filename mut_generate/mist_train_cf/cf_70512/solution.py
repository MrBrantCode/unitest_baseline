"""
QUESTION:
Implement a function named `find_max` that takes an array of integers as input and returns a tuple containing the maximum element and its index in the array. The function should not use any built-in max/min functions or methods.
"""

def find_max(arr):
    max_val = arr[0]
    max_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
    return max_val, max_idx