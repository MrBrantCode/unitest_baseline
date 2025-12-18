"""
QUESTION:
Write a function named `binomial_coefficients` that takes an integer `n` as input and returns a list of binomial coefficients for `n`, where the i-th element in the list corresponds to the coefficient of the i-th term in the expansion of (x+y)^n. The function should return all coefficients for terms from 0 to n.
"""

import math

def binomial_coefficients(n):
    """
    Returns a list of binomial coefficients for n, 
    where the i-th element in the list corresponds 
    to the coefficient of the i-th term in the expansion of (x+y)^n.
    
    Args:
        n (int): The power of the binomial expansion.
    
    Returns:
        list: A list of binomial coefficients.
    """
    coefficients = []
    for i in range(n+1):
        coefficients.append(int(math.factorial(n) / (math.factorial(i)*math.factorial(n-i))))
    return coefficients