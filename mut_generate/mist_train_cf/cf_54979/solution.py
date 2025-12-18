"""
QUESTION:
Write a function named `generate_sequence` that generates a sequence of integers starting from 0 and increasing by 1 up to a specified size `n`. The function should return a list of integers. Additionally, create a function `get_element_at_index` that takes a list and an index as input and returns the element at the specified index if it exists, otherwise it should return an error message and `None`. Both functions should be able to handle any given size of array and index values. The generated sequence should support retrieval of elements based on their index values.
"""

def generate_sequence(n):
    """Generate a sequence of integers from 0 to n-1."""
    return [i for i in range(n)]

def get_element_at_index(array, index):
    """Retrieve an element at a specified index from the given array."""
    if index < len(array):
        return array[index]
    else:
        print("Index out of range!")
        return None