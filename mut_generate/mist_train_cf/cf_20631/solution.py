"""
QUESTION:
Write a function `sort_array(lst)` that takes a list of integers as input, checks if it contains only positive integers and has a length of at least 5, converts the list into a numpy array, finds the sum of all elements, sorts the array in descending order, and returns the sorted array.
"""

import numpy as np

def sort_array(lst):
    # Check if the input list meets the requirements
    if len(lst) < 5:
        return "Input list should have a length of at least 5."
    for num in lst:
        if not isinstance(num, int) or num <= 0:
            return "Input list should contain only positive integers."

    # Convert the list into a numpy array
    arr = np.array(lst)

    # Find the sum of all elements
    total_sum = np.sum(arr)

    # Sort the array in descending order
    sorted_arr = np.sort(arr)[::-1]

    return sorted_arr