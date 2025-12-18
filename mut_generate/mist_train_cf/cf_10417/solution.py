"""
QUESTION:
Find the indices of all occurrences of a given element in an array. The function should be named `find_element_indices` and it should take two parameters: an array and an element. The function should return a list of indices where the element is found in the array. Note that the array can contain duplicates of the element.
"""

def find_element_indices(array, element):
    return [i for i, x in enumerate(array) if x == element]