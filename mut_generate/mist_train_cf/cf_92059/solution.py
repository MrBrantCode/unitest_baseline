"""
QUESTION:
Calculate the power of two numbers using only basic arithmetic operations. 

Write a function `power(base, exp)` that calculates the value of `base` raised to the power of `exp` without using built-in exponentiation or logarithmic functions. The function should be able to handle negative exponents.
"""

def power(base, exp):
    result = 1

    if exp < 0:
        base = 1 / base
        exp = -exp

    for _ in range(exp):
        result *= base

    return result