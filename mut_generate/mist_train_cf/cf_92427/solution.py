"""
QUESTION:
Write a function named `reverse_array` that takes an array of length n as an argument, and returns the input array with its elements in reverse order. The function should only use constant extra space and have a time complexity of O(n).
"""

def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    return arr