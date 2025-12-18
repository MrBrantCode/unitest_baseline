"""
QUESTION:
Implement a function called `quicksort` that takes a list of integers as input, sorts the list in ascending order, and returns the sorted list. The function should use the Quicksort algorithm, have an average-case time complexity of O(n log n), and handle recursion without causing a stack overflow error for large input sizes.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)