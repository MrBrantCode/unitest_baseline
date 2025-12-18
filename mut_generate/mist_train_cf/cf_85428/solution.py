"""
QUESTION:
Create a function `matrix_multiplication(A, B)` that takes two 2D numpy arrays `A` and `B` as input and returns their product using matrix multiplication rules. The function should handle the case where `A` and `B` cannot be multiplied due to incompatible dimensions, and in such cases, it should print an error message and return `None`. The number of columns in `A` must be equal to the number of rows in `B` for the multiplication to be successful.
"""

import numpy as np

def matrix_multiplication(A, B):
    try:
        result = np.dot(A, B)
        return result
    except ValueError as e:
        print("Error: ",str(e))
        return None