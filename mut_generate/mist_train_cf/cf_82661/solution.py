"""
QUESTION:
Create a function to access and modify elements in a 3x3x3x3x3 5D array initialized with -1. The function should take a 5D coordinate (tuple of 5 integers) and an optional new value to change the existing value at the given coordinate. Implement two functions: `access_value` to retrieve the value at the specified coordinate and `change_value` to modify the value at the specified coordinate.
"""

import numpy as np

# Formulate a 5D array of size 3 x 3 x 3 x 3 x 3 where every element corresponds to -1
array = np.full((3, 3, 3, 3, 3), -1)

def access_and_change_value(coords, new_value=None):
    if new_value is not None:
        array[coords] = new_value
    return array[coords]