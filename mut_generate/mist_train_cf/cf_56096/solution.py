"""
QUESTION:
Define the function `M(p)` to determine the maximum value of `n` for which the denominator of the `n`-th harmonic number is not a multiple of `p`. The `n`-th harmonic number is the cumulative sum of the reciprocals of the first `n` positive integers, expressed as a reduced fraction. The function should return the value of `n-1` when the denominator of the `n`-th harmonic number is a multiple of `p`.
"""

import fractions

def M(p):
    s = fractions.Fraction(0)
    n = 1
    while True:
        s += fractions.Fraction(1,n)
        if s.denominator % p == 0:
            return n-1
        n += 1