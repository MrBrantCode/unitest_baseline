"""
QUESTION:
Implement a function `can_reconstruct_dtype` that determines whether a given list of field names and data types can be used to reconstruct a NumPy dtype without requiring any additional parameters. The function should take two parameters: `field_names` (a list of strings representing field names) and `dtypes` (a list of data types). It should return True if the dtype can be reconstructed from the provided list, and False otherwise.
"""

from typing import List
import numpy as np

def can_reconstruct_dtype(field_names: List[str], dtypes: List[type]) -> bool:
    dtype = {name: dtype for name, dtype in zip(field_names, dtypes)}
    try:
        reconstructed_dtype = np.dtype([(name, dtype) for name, dtype in dtype.items()])
        return np.array_equal(reconstructed_dtype, np.dtype({ 'names': field_names, 'formats': dtypes }))
    except ValueError:
        return False