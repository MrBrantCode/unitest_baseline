"""
QUESTION:
Write a function called `find_indices` that finds the indices of all occurrences of a specified element in an array. The function should take an array `arr` and an element as input, and return a list of indices where the element is found. If the element is not found in the array, return -1. Assume that the array and the element are of valid types.
"""

def find_indices(arr, element):
    indices = []
    for i in range(len(arr)):
        if arr[i] == element:
            indices.append(i)
    if len(indices) == 0:
        return -1
    return indices