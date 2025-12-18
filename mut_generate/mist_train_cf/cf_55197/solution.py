"""
QUESTION:
Write a function named `swap_elements` that takes an array of arbitrary length and data type as input. The function should swap the first and last elements, the second and second-to-last elements, the third and third-to-last elements, and so on. If the array has only one element, return the array as is.
"""

def swap_elements(arr):
    # Check if the array has more than 1 element
    if len(arr) > 1:
        # Copy the array in reversed order and return
        return arr[::-1]
    # Otherwise return the array as is
    return arr