"""
QUESTION:
Implement a function `transform_to_structured_array` that transforms a given list of integers into a structured numpy array. The array should have three fields: 'Value' of type integer, 'Square Root' of type float, and 'String Equivalent' of type string, representing the original values, their respective square roots, and their string equivalents. Optimize the solution for time and space complexity.
"""

import numpy as np

def transform_to_structured_array(values):
    dtype = [('Value', int), ('Square Root', float), ('String Equivalent', 'U20')]
    structured_array = np.empty(len(values), dtype=dtype)

    for i, value in enumerate(values):
        structured_array[i] = (value, np.sqrt(value), str(value))
    
    return structured_array