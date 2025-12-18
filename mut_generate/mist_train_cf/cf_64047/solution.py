"""
QUESTION:
Write a function named `complex_matrix_operation` that accepts a complex number `comp_num` and a 2D matrix `comp_matrix` of complex numbers as parameters. The function should return the conjugate of `comp_num` and the result of multiplying `comp_matrix` by `comp_num`, with a time complexity of O(n^2) for an nxn matrix.
"""

import numpy as np

def complex_matrix_operation(comp_num, comp_matrix):
    """
    This function calculates the conjugate of a given complex number and 
    multiplies a 2D matrix of complex numbers by the given complex number.

    Parameters:
    comp_num (complex): The complex number.
    comp_matrix (numpy array): A 2D matrix of complex numbers.

    Returns:
    tuple: A tuple containing the conjugate of comp_num and the result of 
    multiplying comp_matrix by comp_num.
    """
    comp_conjugate = np.conj(comp_num)
    manipulated_matrix = np.multiply(comp_matrix, comp_num)
    return comp_conjugate, manipulated_matrix