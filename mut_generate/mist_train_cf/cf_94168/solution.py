"""
QUESTION:
Write a function `find_indices(arr, element)` that takes an array `arr` and an `element` as input and returns a list of indices where the `element` is found in the array. If the `element` is not found, return -1.
"""

def find_indices(arr, element):
    indices = [i for i in range(len(arr)) if arr[i] == element]
    return indices if indices else -1