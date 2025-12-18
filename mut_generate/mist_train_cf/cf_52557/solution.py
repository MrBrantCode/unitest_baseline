"""
QUESTION:
Write a function named `derivative_and_integral` that takes a list of coefficients `xs` defining a polynomial and an integer `C` as input, and returns the coefficients of the polynomial's derivative and integral. The derivative and integral should be returned as a tuple of two lists, where the first list represents the coefficients of the derivative and the second list represents the coefficients of the integral with the constant `C`.
"""

def derivative_and_integral(xs: list, C: int):
    derivative = [i*x for i,x in enumerate(xs)][1:]  # skip the first term since the derivative of a constant is 0
    integral = [C]+[x/(i+1) for i,x in enumerate(xs)] # prepend the constant C and calculate the integral
    return derivative, integral