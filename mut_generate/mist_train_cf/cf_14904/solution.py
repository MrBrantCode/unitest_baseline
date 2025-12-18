"""
QUESTION:
Create a function named `search_indices` that takes an array and an element as input. The array may contain duplicate elements. The function should return a list of indices of all occurrences of the given element in the array.
"""

def search_indices(array, element):
    indices = []
    for i in range(len(array)):
        if array[i] == element:
            indices.append(i)
    return indices