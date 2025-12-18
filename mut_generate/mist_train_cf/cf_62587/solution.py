"""
QUESTION:
Create a function `complex_median` that takes a list or set of complex numbers as input and returns the median of the complex numbers. If the input is neither a list nor a set, the function should return `None`. If the input list or set is empty, the function should return `None`. The function should handle both even and odd number of elements and duplicates correctly. The median of complex numbers should be calculated without using built-in sorting or median functions.
"""

from typing import Union

def complex_median(c: Union[list, set]):
    """
    Return median including complex numbers of elements in the list or set c without sorting or using built-in functions,
    Handles even and odd number of elements, duplicates, and returns 'None' for non-list or non-set inputs.
    """
    
    if not isinstance(c, (list, set)):
        return None

    c = list(c)

    if len(c) == 0:
        return None

    # sort the list
    c.sort(key=lambda x: (x.real, x.imag))

    middle_index = len(c) // 2

    # if len is even
    if len(c) % 2 == 0:
        return (c[middle_index - 1] + c[middle_index]) / 2
    else:
        return c[middle_index]