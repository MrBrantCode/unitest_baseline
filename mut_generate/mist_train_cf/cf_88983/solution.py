"""
QUESTION:
Write a function named `reverse_array` that takes an array of length n as input, reverses its elements in-place without using any extra space that scales with input size, and returns the modified array. The function must have a time complexity of O(n).
"""

def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr