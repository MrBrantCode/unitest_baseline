"""
QUESTION:
Implement a function `multiply_largest_integers(lst)` that takes a list of numerical values (including floating point numbers and negatives) and returns the product of the largest integer less than or equal to each absolute value. 

The function should handle empty lists by returning 0, throw a warning if the list contains non-numerical values, and return 0 for lists where no valid integer is extracted from the numbers after applying floor of absolute values.
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