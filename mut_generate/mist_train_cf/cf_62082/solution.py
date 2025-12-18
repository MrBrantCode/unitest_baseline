"""
QUESTION:
Write a function named `catalan(n)` that calculates the nth Catalan number using the formula C(n) = (2n)! / ((n+1)! * n!), where n is a non-negative integer. The function should handle the case where n is 0 or 1, for which the Catalan number is defined as 1. Use the math.factorial function to compute the factorials and perform integer division to prevent floating point results.
"""

import math

def catalan(n):
    if n <= 1:
        return 1
    else:
        return math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))