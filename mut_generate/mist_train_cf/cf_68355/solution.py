"""
QUESTION:
Write a function `complex_median` that calculates the median of a list or set of complex numbers or integers. The function should handle both even and odd number of elements, duplicates, and non-sortable data types. It should return the median value if the input is a list or set, and 'None' otherwise. The function should not use built-in median functions. Note that a built-in sort function can be used for sorting the input data. 

The input can be a list or set of integers or complex numbers. The function should be able to handle cases where the input is neither a list nor a set. The output should be a complex number or integer representing the median value, or 'None' if the input is invalid.
"""

from typing import Union

def complex_median(l: Union[list, set]):
    """
    Return median including complex numbers of elements in the list or set l without using built-in median functions.
    Handles even and odd number of elements, duplicates and returns 'None' for non-list or non-set inputs.
    """
    
    if not isinstance(l, (list, set)):
        return None
        
    l = list(l)

    if len(l) == 0:
        return None
        
    # sort the list
    l.sort(key=lambda c: (c.real, c.imag) if isinstance(c, complex) else (c, 0))

    middle_index = len(l) // 2

    # if length is even
    if len(l) % 2 == 0:
        return (l[middle_index - 1] + l[middle_index]) / 2
    else:
        return l[middle_index]