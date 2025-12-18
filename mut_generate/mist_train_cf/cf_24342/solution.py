"""
QUESTION:
Create a function `calculate_e(n)` that calculates the value of "e" to the nth term, where "e" is the base of the natural logarithm, approximately equal to 2.71828, and is calculated using the infinite series 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!. The function should take an integer `n` as input and return the calculated value of "e" to the nth term.
"""

import math

def calculate_e(n): 
    e = 0
    for i in range(n + 1): 
        e += 1 / math.factorial(i) 
    return e