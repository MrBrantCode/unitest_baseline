"""
QUESTION:
Write a function `linear_search` that performs a linear search in an array of integers for a target element and returns the indices of all its occurrences. The function should return an empty list if the target element is not found. The input array and the target element will be provided as parameters to the function.
"""

def linear_search(array, target):
    indices = []
    for i in range(len(array)):
        if array[i] == target:
            indices.append(i)
    return indices