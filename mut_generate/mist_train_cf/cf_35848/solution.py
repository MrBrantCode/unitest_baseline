"""
QUESTION:
Create a function named `create_arrays` that takes two parameters: `l_tot` and `num_time_samples`. The function should create two NumPy arrays, `second_row` and `first_row`, based on the given parameters and return them. The `second_row` array should be created by concatenating an array of zeros of length `l_tot-1` with an array filled with the value `num_time_samples` of length `l_tot-1`. The `first_row` array should be created by concatenating the value `0` with an array filled with the value `num_time_samples` of length `l_tot-1`.
"""

import numpy as np

def entance(l_tot, num_time_samples):
    second_row = np.concatenate([np.zeros(l_tot-1), np.full(l_tot-1, num_time_samples)])
    first_row = np.concatenate([[0], np.full(l_tot-1, num_time_samples)])
    return second_row, first_row