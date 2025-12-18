"""
QUESTION:
Create a function named `cumulative_binomial_product` that calculates the cumulative product of binomial coefficients. The function should take one argument `n` which can be an integer, a floating point number, a complex number, a list, or a tuple. The function should return an error message if the input is invalid. If `n` is a list or tuple, calculate the cumulative product of binomial coefficients for each element in the list/tuple. If `n` is an integer, calculate the cumulative product of binomial coefficients from 0 to `n`. Binomial coefficients are not defined for floating point and complex numbers, so return an error message in these cases.
"""

import math
import functools
import operator

def cumulative_binomial_product(n):
    if type(n) not in (int, list, tuple):
        return "Invalid input. Please enter an integer, a list or a tuple."

    if type(n) == int and n < 0:
        return "Invalid input. Please enter a non-negative integer."

    if type(n) in (list, tuple):
        try:
            cumulative_product = 1
            for i in n:
                if i < 0 or type(i) != int:
                    return "Invalid input in list/tuple. Please ensure all elements are non-negative integers."

                if i > 0: 
                    cumulative_product *= functools.reduce(operator.mul, (math.comb(i, j) for j in range(i+1)), 1)
            return cumulative_product
        except TypeError:
            return
    elif type(n) == int:
        return functools.reduce(operator.mul, (math.comb(n, i) for i in range(n+1)), 1)