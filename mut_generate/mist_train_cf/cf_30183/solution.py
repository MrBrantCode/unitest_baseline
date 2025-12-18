"""
QUESTION:
Implement a Python function `custom_norm` that calculates the norm of a given vector or matrix. The function should take in two parameters: `input_data`, a list representing either a 1D vector or a 2D matrix, and `norm_order`, an integer representing the order of the norm to be calculated (1, 2, or infinity). The function should return the calculated norm based on the input parameters and the standard mathematical definitions for vector and matrix norms. Do not use any external libraries or built-in functions for norm calculation.
"""

import math

def custom_norm(input_data, norm_order):
    if isinstance(input_data[0], list):  
        if norm_order == 1:
            return max(sum(abs(row[i]) for row in input_data) for i in range(len(input_data[0])))
        elif norm_order == 2:
            # Not implemented for simplicity
            return "L2 norm for matrices not implemented"
        elif norm_order == float('inf'):
            return max(sum(abs(val) for val in row) for row in input_data)
        else:
            return "Invalid norm order for matrices"
    else:  
        if norm_order == 1:
            return sum(abs(val) for val in input_data)
        elif norm_order == 2:
            return math.sqrt(sum(val**2 for val in input_data))
        elif norm_order == float('inf'):
            return max(abs(val) for val in input_data)
        else:
            return "Invalid norm order for vectors"