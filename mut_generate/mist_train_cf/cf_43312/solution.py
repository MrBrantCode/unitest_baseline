"""
QUESTION:
Write a function `check_and_coerce` that takes a single argument `X` and returns a boolean indicating whether `X` is a list, tuple, or NumPy array, along with the coerced `X` as a NumPy array if it was originally a list or tuple. The function should work with the following restrictions: 
- If `X` is a list or tuple, it should be coerced into a NumPy array.
- If `X` is already a NumPy array, it should be left unchanged.
- If `X` is neither a list, tuple, nor NumPy array, the function should return `False` and `X` as is.
"""

import numpy as np

def check_and_coerce(X):
    """
    Checks if the input is a list, tuple, or NumPy array, and coerces it into being one with np.array(X).
    
    Args:
    X: Input data which can be a list, tuple, or NumPy array.
    
    Returns:
    bool: Indicates whether the input is a list, tuple, or NumPy array.
    np.ndarray: The coerced input as a NumPy array if applicable.
    """
    is_list_tuple_array = isinstance(X, (list, tuple, np.ndarray))
    if is_list_tuple_array and not isinstance(X, np.ndarray):
        X = np.array(X)
    return is_list_tuple_array, X