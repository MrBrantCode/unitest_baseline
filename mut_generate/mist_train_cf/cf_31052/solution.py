"""
QUESTION:
Implement a function `validate_pvalues(pvals)` that takes a NumPy array `pvals` of p-values as input. The function should check that the array contains no NaN values, all values are within the range (0, 1), and no value is exactly 0 or 1. Return True if all checks pass, and False otherwise.
"""

import numpy as np

def validate_pvalues(pvals):
    # check for NA
    if np.isnan(pvals).any():
        return False
    # check range
    if (((pvals < 0).sum() + (pvals > 1).sum()) > 0):
        return False

    # check for p-values that are either exactly 0 or 1
    if (pvals == 0.).any() or (pvals == 1.).any():
        return False

    return True