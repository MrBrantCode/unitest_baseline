"""
QUESTION:
Write a function named `factor(x)` that returns a list of all the factors of a given positive integer `x`. The function should find all numbers from 1 to `x` that divide `x` without leaving a remainder.
"""

def factor(x): 
    factors = []
    for i in range(1, x + 1): 
        if x % i == 0: 
            factors.append(i) 
    return factors