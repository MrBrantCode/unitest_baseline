"""
QUESTION:
Write a function `calculate(expression)` that evaluates a string mathematical expression with support for exponentiation, modulo, root calculation, floating point numbers, and scientific notation. The function should follow the order of operations and handle errors for negative roots and undefined modulo operations.
"""

import cmath
import math

def calculate(expression):
    try:
        # Try to evaluate the expression as a real number
        return eval(expression)
    except Exception as e:
        try:
            # If the above fails, try to evaluate it as a complex number
            return complex(expression)
        except Exception as e:
            # If all fails, then print an error message
            raise Exception(f'Error: Invalid expression. {e}')