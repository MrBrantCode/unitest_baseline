"""
QUESTION:
Implement a function `generate_combined_array(start, end, num_first, num_second)` that generates two sets of evenly spaced numbers within a given range and combines them into a single array. The first set should contain `num_first` elements from the start of the range to the midpoint (exclusive), while the second set should contain `num_second` elements from the midpoint (inclusive) to the end of the range (inclusive). The midpoint is calculated based on the proportion of `num_first` to the total number of elements. The function should return the combined array of these two sets of numbers.
"""

import numpy as np

def generate_combined_array(start, end, num_first, num_second):
    midpoint = start + (end - start) * (num_first / (num_first + num_second))
    first_set = np.linspace(start, midpoint, num_first, endpoint=False)
    second_set = np.linspace(midpoint, end, num_second, endpoint=True)
    combined_array = np.concatenate((first_set, second_set))
    return combined_array