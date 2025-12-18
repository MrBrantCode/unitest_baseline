"""
QUESTION:
Create a function called `derivative_integral_and_zeros` that takes a list `xs` representing the coefficients of a polynomial and an integer `C` representing the integral constant. The function should return a tuple containing the coefficients of the derivative of the polynomial, the coefficients of the integral of the polynomial (including the constant `C`), and the zeros of the polynomial. 

The polynomial is represented as `xs[0] + xs[1] * x + xs[2] * x^2 + ...`. The function should handle polynomials of any degree and return the zeros as a list of complex numbers. The function should use the `numpy` library to calculate the zeros of the polynomial.
"""

import numpy as np

def derivative_integral_and_zeros(xs: list, C: int):
    num_coeff = len(xs)
    
    # Calculate derivative
    derivative = [i * xs[i] for i in range(1, num_coeff)]
    
    # Calculate integral
    integral = [xs[i] / (i + 1) for i in range(num_coeff)]
    integral.insert(0, C)  # Include `C`
    
    # Calculate zeros
    zeros = np.roots(list(reversed(xs))).tolist()
    
    return derivative, integral, zeros