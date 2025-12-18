"""
QUESTION:
Implement the `is_float(dtype)` function to return `True` if the given NumPy data type `dtype` represents a floating-point number and `False` otherwise. Implement the `is_number(dtype)` function to return `True` if the given NumPy data type `dtype` represents a general numeric type (including integer, floating-point, and complex) and `False` otherwise.
"""

import numpy as np

def is_float(dtype):
    """Return True if datatype dtype is a float kind"""
    return np.issubdtype(dtype, np.floating)

def is_number(dtype):
    """Return True if datatype dtype is a number kind"""
    return np.issubdtype(dtype, np.number)