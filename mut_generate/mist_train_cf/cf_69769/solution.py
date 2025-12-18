"""
QUESTION:
Create a function called `calculate_median` that calculates the median of a list of string numbers, some of which may be 'nan' (representing NaN or Not a Number), without using loops. The function should convert the string numbers to a suitable format for median calculation and handle 'nan' correctly.
"""

import pandas as pd
import numpy as np

def calculate_median(numbers):
    """
    Calculate the median of a list of string numbers, handling 'nan' correctly.

    Args:
        numbers (list): A list of string numbers.

    Returns:
        float: The median of the input numbers.
    """
    NB = pd.to_numeric(numbers, errors='coerce')
    return np.nanmedian(NB)