"""
QUESTION:
Write a function `M(p)` that takes a prime number `p` as input and returns the maximum value of `n` for which the denominator of the harmonic number `H_n = 1/1 + 1/2 + ... + 1/n` is not a multiple of `p`.
"""

import fractions

def M(p):
    harmonic_number = fractions.Fraction(0)
    n = 1
    while harmonic_number.denominator % p != 0:
        harmonic_number += fractions.Fraction(1, n)
        n += 1
    return n - 1