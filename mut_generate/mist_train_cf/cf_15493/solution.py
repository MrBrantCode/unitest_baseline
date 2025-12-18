"""
QUESTION:
Write a function `max_product(arr)` that takes an array of integers as input and returns the maximum product of four integers in the array. The function should work for arrays with at least four elements, and the product can be obtained by multiplying any four integers in the array.
"""

def max_product(arr):
    arr.sort()
    n = len(arr)
    return max(arr[n-1] * arr[n-2] * arr[n-3] * arr[n-4], arr[0] * arr[1] * arr[2] * arr[n-1])