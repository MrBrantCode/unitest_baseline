"""
QUESTION:
Design a function named `geometric_mean` that takes two lists of integers and/or floats, possibly with null values and of different lengths, and returns their geometric mean as a float. The function should ignore null values and handle the case where the input lists contain only null values.
"""

from typing import List, Union
import numpy as np

def geometric_mean(arr1: List[Union[int, float]], arr2: List[Union[int, float]]) -> float:
    combined = arr1 + arr2
    combined = [value for value in combined if value is not None]
    if len(combined) > 0:
        product = np.prod(combined)
        return product ** (1.0/len(combined))
    else:
        return None