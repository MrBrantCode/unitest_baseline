"""
QUESTION:
Write a function named `find_min` that takes an array of integers as input and returns the minimum element in the array without using the built-in `min()` function. The function should assume that the input array is non-empty.
"""

def find_min(arr):
    min_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
    return min_element