"""
QUESTION:
Write a function `reverse_array` that takes an array of length `n` as input and returns the array with its elements in reverse order. The function should use constant extra space and have a time complexity of O(n).
"""

def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    return arr