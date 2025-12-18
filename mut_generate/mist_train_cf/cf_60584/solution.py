"""
QUESTION:
Write a function called `smallest_product` that takes an array of at least 5 integers as input. The function should return the smallest product that can be obtained by multiplying a pair of integers in the array.
"""

def smallest_product(arr):
    arr.sort()
    return min(arr[0] * arr[1], arr[-1] * arr[-2])