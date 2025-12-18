"""
QUESTION:
Design a function named `factorial_of_tuple_elements` that takes a tuple and a list as input. The function should calculate the factorial of each integer value in the tuple, including those in nested tuples, round floating point numbers to the nearest integer before calculation, ignore non-numeric data types and non-positive integers, and append the results to the given list. If the input tuple is empty, the function should return an error message.
"""

import math
import itertools
from typing import Tuple, List

def factorial_of_tuple_elements(tup: Tuple, result: List):
    """
    Calculate factorials of all integer values in a tuple (including nested tuples) and 
    append them to a specified list. Non-integer types and non-positive integers are ignored.
   
    Args:
      tup: Tuple with nested tuples and integer values.
      result: Original list to append the factorials to.
   
    Returns:
      A list with factorials of all integer values found in the tuple.
    """
    if tup == ():
        return 'Error: Tuple is empty.'
    else:
        flattened = list(itertools.chain.from_iterable([[i] 
        if not isinstance(i, tuple) else list(i) for i in tup]))
        for i in flattened:
            if isinstance(i, int) and i >= 0:
                result.append(math.factorial(i))
            elif isinstance(i, float) and i >= 0:
                result.append(math.factorial(round(i)))
    return result