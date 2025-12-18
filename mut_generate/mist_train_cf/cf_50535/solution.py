"""
QUESTION:
Write a function F(n, d) that calculates the number of divisors of n! that end with the digit d, modulo (10^16 + 61). The input n is a non-negative integer and d is a positive integer. Your function should be able to handle a large input n up to 10^6.
"""

import math

def entrance(n, d):
    # Calculate the number of divisors of n! that end with d
    count_2 = 0
    i = 5
    while (n / i >= 1):
        count_2 += int(n / i)
        i *= 5
    # Compute this number modulo (10^16 + 61)
    return pow(2, count_2, int(math.pow(10, 16) + 61))