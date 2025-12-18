"""
QUESTION:
Create a function called `find_indices(array)` that takes an array of integers as input and returns a sorted list of indices of unique elements in the array, excluding duplicates. The function must have a time complexity of O(n), where n is the length of the array.
"""

def find_indices(array):
    indices = {}
    for i in range(len(array)):
        if array[i] not in indices:
            indices[array[i]] = i
    return sorted(indices.values())