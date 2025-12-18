"""
QUESTION:
Write a function `reverseArray(arr, start, end)` that reverses the given array in-place without using any loops or built-in array manipulation functions. The function must have a time complexity of O(1) and cannot create a new array to store the reversed elements. The array can contain up to 10^5 elements.
"""

def reverseArray(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseArray(arr, start + 1, end - 1)