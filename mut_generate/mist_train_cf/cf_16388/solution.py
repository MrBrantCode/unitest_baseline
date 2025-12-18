"""
QUESTION:
Write a function `modulo_without_operator` that takes two positive integers `n1` and `n2` as input and returns the remainder of `n1` divided by `n2` without using the modulus operator. Ensure the function handles cases where `n2` is negative by treating it as its absolute value. The function should return an integer result.
"""

def modulo_without_operator(n1, n2):
    # Ensure n2 is positive
    n2 = abs(n2)
    
    # Divide n1 by n2 and round to the nearest integer
    result = round(n1 / n2)
    
    # Multiply n2 with the rounded result and subtract it from n1
    n1 -= n2 * result
    
    return n1