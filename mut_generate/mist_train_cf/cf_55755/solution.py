"""
QUESTION:
Write a function `find_smallest` that uses recursion to find the smallest element in an array of integers and its index. The function should take as parameters the array and the current index, and return the smallest element and its index. The array may contain duplicate integers and should not use any built-in or library functions. The function should handle cases where the array is empty.
"""

def find_smallest(arr, idx, min_val, min_idx):
    if idx == len(arr):
        return min_val, min_idx

    if arr[idx] < min_val:
        min_val, min_idx = arr[idx], idx

    return find_smallest(arr, idx+1, min_val, min_idx)

def find_smallest_wrapper(arr):
    if len(arr) < 1:
        return None
    else:
        return find_smallest(arr, 0, arr[0], 0)