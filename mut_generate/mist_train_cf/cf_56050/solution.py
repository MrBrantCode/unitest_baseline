"""
QUESTION:
Implement a function named `accumulate_product` that takes a 4D tensor of diverse dimensions and types of data, and returns the accumulative product of all its non-zero entries. The function should be flexible to accommodate tensors of varying dimensions and data types. 

The function should include a robust error-checking mechanism that handles cases of zero-valued tensor entries by raising an exception, and supports non-zero integers and floating point numbers.
"""

import numpy as np

def accumulate_product(tensor):
    if isinstance(tensor, list):
        if len(tensor) == 0:
            return 1  # Return neutral element for multiplication
        else:
            head, *tail = tensor
            return accumulate_product(head) * accumulate_product(tail)
    else:
        if tensor == 0:
            raise Exception("Zero-valued tensor entry. Caution: Division by zero in subsequent computations")
        else:
            return tensor