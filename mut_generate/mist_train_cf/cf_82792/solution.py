"""
QUESTION:
Write a function `derivative` that calculates the derivative of an exponential series represented by coefficients in the input list `xs`. The function should take a list of coefficients as input and return a list of the same length, where each element is the derivative of the corresponding term in the exponential series. The derivative of each term `xs[i] * e^(x/(i+1))` is `(i+1)/1 * xs[i] * e^(x/(i+1))`. The function should work for any input list of coefficients.
"""

import math

def derivative(xs):
    return [i * x for i, x in enumerate(xs, start=1)]