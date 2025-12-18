"""
QUESTION:
Implement the `quicksort` function, which sorts an unordered array of integers in ascending order, minimizing memory usage and time complexity. The function should handle potential integer overflows.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)