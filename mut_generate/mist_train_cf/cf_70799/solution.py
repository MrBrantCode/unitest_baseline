"""
QUESTION:
Create a function named `power` that calculates the exponentiation of a number `n` raised to a power `m` without using the `**` operator or any built-in exponentiation functions. The function should handle both positive and negative values of `m`, but not fractional exponents. The function should use recursion to compute the result.
"""

def power(n, m):
    if m == 0:
        return 1
    elif m > 0: 
        return n * power(n, m-1)
    elif m < 0: 
        return 1/n * power(n, m+1)