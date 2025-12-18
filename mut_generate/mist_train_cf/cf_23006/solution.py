"""
QUESTION:
Create a function called `search_indices` that takes an array and an element as input, and returns a list of indices where the element appears in the array. The function should return all indices in ascending order. The array may contain duplicate elements.
"""

def search_indices(array, element):
    return [i for i, x in enumerate(array) if x == element]