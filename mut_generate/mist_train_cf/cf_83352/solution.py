"""
QUESTION:
Write a function `cumulative_binomial_product(n)` that calculates the cumulative product of consecutive binomial coefficients within a given range `n`. The function should accept a positive integer `n`, a list of positive integers, or a tuple of positive integers. If `n` is a list or tuple, calculate the cumulative product for each integer and return the product of these products. The function should return an error message if `n` is not a positive integer, a list of positive integers, or a tuple of positive integers, or if it contains non-integer, negative, or non-positive values.
"""

import math
import functools
import operator

def cumulative_binomial_product(n):
    if type(n) not in (int, list, tuple):
        return "Invalid input. Please enter a positive integer, a list or a tuple."

    if type(n) in (list, tuple):
        try:
            cumul_product = 1
            for i in n:
                if i < 1 or type(i) != int:
                  return "Invalid input in list/tuple. Please assure all elements are positive integers."
                  
                if i > 0: 
                    cumul_product *= functools.reduce(operator.mul, (math.comb(i, j) for j in range(i+1)), 1)
            return cumul_product
        except TypeError:
            return
    elif type(n) == int:
        if n < 1:
            return "Invalid input. Please enter a positive integer."
        return functools.reduce(operator.mul, (math.comb(n, i) for i in range(n+1)), 1)