"""
QUESTION:
Design a program with three functions: `complex_operations`, `matrix_operations`, and `modulo_OPERATION`. 

The `complex_operations` function should take three parameters: two complex numbers `z1` and `z2`, and a string `operation`. It should perform the specified operation (addition, subtraction, multiplication, division, exponentiation, or root calculation) on the complex numbers and return the result. It should handle division by zero and invalid operations.

The `matrix_operations` function should take three parameters: two 2D matrices `m1` and `m2`, and a string `operation`. It should perform the specified operation (addition, subtraction, or multiplication) on the matrices and return the result. It should handle non-conformable matrices for the operation.

The `modulo_OPERATION` function should take two parameters: two numbers `a` and `b`, and return the remainder of `a` divided by `b`. It should handle division by zero. The program should be optimized to handle large numbers efficiently.
"""

import cmath
import numpy as np

def complex_operations(z1, z2, operation):
    if operation == "add":
        return z1 + z2
    elif operation == "subtract":
        return z1 - z2
    elif operation == "multiply":
        return z1 * z2
    elif operation == "divide":
        try:
            return z1 / z2
        except ZeroDivisionError:
            return "Error: Division by zero is not possible."
    elif operation == "exponentiation":
        return z1 ** z2
    elif operation == "root":
        return z1 ** (1/z2)
    else:
        return "Error: Invalid input."

def matrix_operations(m1,m2,operation):
    try:
        if operation == "add":
            return np.add(m1,m2)
        elif operation == "subtract":
            return np.subtract(m1,m2)
        elif operation == "multiply":
            return np.dot(m1,m2)
        else:
            return "Error: Invalid operation."
    except ValueError:
        return "Error: Matrices are non-conformable for the operation."
    
def modulo_OPERATION(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Error: Division by zero is not possible."