"""
QUESTION:
Write a function called `base_2_logarithm` that calculates the base-2 logarithm of a given positive integer using only bitwise operations. The input integer is guaranteed to be greater than 0.
"""

def entance(n):
    log = 0
    while n > 1:
        n = n >> 1
        log += 1
    return log