"""
QUESTION:
Write a function `find_indices` that takes an array `arr` and an element as input and returns a list of indices where the element is found in the array. If the element is not found, return an empty list. The function should only return the indices where the exact match is found.
"""

def find_indices(arr, element):
    indices = []
    for i in range(len(arr)):
        if arr[i] == element:
            indices.append(i)
    return indices