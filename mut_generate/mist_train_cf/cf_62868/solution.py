"""
QUESTION:
Implement a function named `component_wise_modulus` that takes two NumPy arrays of integers as input, performs a component-wise modulus operation, and returns the result. The function should return an error message if the input arrays are not of the same shape, if the input arrays are not of integer type, or if the second array contains null values.
"""

import numpy as np

def component_wise_modulus(array1, array2):
    if not isinstance(array1, np.ndarray) or not isinstance(array2, np.ndarray):
        return 'Error: input is not a paired element'
    
    if array1.shape != array2.shape:
        return 'Error: paired elements diverge in extent'
    
    if np.issubdtype(array1.dtype, np.integer) == False or np.issubdtype(array2.dtype, np.integer) == False:
        return 'Error: paired element constituents are not whole numbers'

    if np.isnan(array2).any():
        return 'Error: second paired element encompasses null values'

    result = np.remainder(array1, array2)
    return result