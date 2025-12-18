"""
QUESTION:
Implement a function `calculate_result_shape(lhs_shape, rhs_shape)` that calculates the resulting shape of a tensor operation. The function takes two input shapes, `lhs_shape` and `rhs_shape`, representing the dimensions of the left-hand side (LHS) and right-hand side (RHS) tensors as lists of integers, and returns the resulting shape after the operation. If the RHS tensor has a single dimension or the same number of dimensions as the LHS tensor, the resulting shape should have the same dimensions as the LHS tensor.
"""

from typing import List

def calculate_result_shape(lhs_shape: List[int], rhs_shape: List[int]) -> List[int]:
    lhs_dim = len(lhs_shape)
    rhs_dim = len(rhs_shape)
    result_shape = [0] * lhs_dim  

    if rhs_dim == 1 or rhs_dim == lhs_dim:
        for i in range(lhs_dim):
            result_shape[i] = lhs_shape[i]

    return result_shape