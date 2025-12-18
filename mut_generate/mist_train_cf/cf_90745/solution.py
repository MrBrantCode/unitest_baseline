"""
QUESTION:
Implement a function `reverse_array` that takes an array of integers as input and returns the array with its elements reversed. The input array will contain at least 5 elements and at most 100 elements, and you cannot use any built-in array reverse functions.
"""

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr