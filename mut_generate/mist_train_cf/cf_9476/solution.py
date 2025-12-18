"""
QUESTION:
Create a function `double_and_sort(arr)` that takes an array of integers as input, doubles the value of each element, and returns a new array with the doubled values in non-decreasing order. The input array can contain up to 10^6 elements and may include both positive and negative integers.
"""

def double_and_sort(arr):
    return sorted([num * 2 for num in arr])