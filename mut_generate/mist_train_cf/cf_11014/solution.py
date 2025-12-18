"""
QUESTION:
Create a function named `generate_sorted_array` that generates a NumPy array of values from a given function `f(x)` within a specified range of x values from 0 to 10 (exclusive) with a step size of 0.5. The function should only apply to x values that are multiples of 3 and include values greater than 0. The resulting array should be sorted in descending order.
"""

import numpy as np

def generate_sorted_array(f):
    x_values = np.arange(0, 10, 0.5)
    filtered_values = [f(x) for x in x_values if x % 3 == 0 and f(x) > 0]
    sorted_values = np.sort(filtered_values)[::-1]
    return sorted_values