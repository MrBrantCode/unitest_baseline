"""
QUESTION:
Write a function `sort_array(lst)` that takes a list of numbers as input and returns the list converted to a numpy array, sorted in descending order. The input list must contain only positive integers and have a length of at least 5.
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

    # Sort the array in descending order
    return np.sort(arr)[::-1]