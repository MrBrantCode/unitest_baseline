"""
QUESTION:
Write a function named `modulo_without_operator` that takes two positive integers `n1` and `n2` as input and returns the remainder of `n1` divided by `n2` without using the modulus operator. The function should ensure the calculation is correct even if `n2` is negative.
"""

def modulo_without_operator(n1, n2):
    # Ensure n2 is positive
    n2 = abs(n2)
    
    # Subtract n2 from n1 until n1 becomes smaller than n2
    while n1 >= n2:
        n1 -= n2
    
    return n1