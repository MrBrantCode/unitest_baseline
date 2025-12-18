"""
QUESTION:
Write a function `max_product` that takes an array of integers as input and returns the maximum product of four integers in the array. The array can contain both positive and negative integers, and the function should handle cases where the maximum product is obtained by multiplying four negative integers or four positive integers. The array will have at least four elements, and the integers can be zero.
"""

def max_product(arr):
    arr.sort()
    n = len(arr)
    return max(arr[n-1] * arr[n-2] * arr[n-3] * arr[n-4], arr[0] * arr[1] * arr[2] * arr[n-1])