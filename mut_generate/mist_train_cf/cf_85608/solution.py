"""
QUESTION:
Implement a function named `BinaryInsertionSort` that sorts a list of integers in ascending order using binary search to determine the insertion point, with a time complexity of O(n log n) and without using any built-in sorting functions. The function should take one parameter `arr`, a list of integers, and return the sorted list.
"""

from bisect import bisect_left

def BinaryInsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = bisect_left(arr, key, 0, i)
        arr = arr[:j] + [key] + arr[j:i] + arr[i+1:]
    return arr