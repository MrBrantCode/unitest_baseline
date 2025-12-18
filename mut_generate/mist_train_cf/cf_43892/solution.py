"""
QUESTION:
Create a function `float_equation` to correctly evaluate a linear equation with floating-point numbers. The function should take two parameters: a slope and a constant c. It should return the result of the equation `(slope * -161) + c`. The function must handle the precision issue of floating-point numbers, ensuring the result is accurate to a high degree of precision.
"""

import math
from decimal import Decimal, getcontext

def float_equation(slope, c):
    # Using math.isclose() function for comparison
    result = (slope * -161) + c
    return result
    
    # Alternatively, using the Decimal module for precision arithmetic operations
    # getcontext().prec = 28 
    # slope = Decimal(slope)
    # c = Decimal(c)
    # result = (slope * -161) + c
    # return result