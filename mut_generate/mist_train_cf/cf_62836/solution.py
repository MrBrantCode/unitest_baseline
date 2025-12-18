"""
QUESTION:
Write a function `multiply_largest_integers(lst)` that takes a list of elements as input. If the list is empty, it should return 0. If the list contains non-numerical values, it should raise a warning and ignore those values. For numerical values, it should take their absolute floor values and multiply them together, but only if at least one non-zero integer exists in the list. If no non-zero integers exist, it should return 0.
"""

import math
import warnings

def multiply_largest_integers(lst):
    if not lst:
        return 0
    
    product = 1
    integer_exists = False   # flag to check if valid integers exist in the list

    for item in lst:
        if not isinstance(item, (int, float)):
            warnings.warn("Non-numerical values detected")
        else:
            val = math.floor(abs(item))
            if val != 0:
                integer_exists = True
                product *= val

    if integer_exists:
        return product

    return 0