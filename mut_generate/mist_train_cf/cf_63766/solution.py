"""
QUESTION:
Given a positive integer n, define f(n) as the cumulative sum of the greatest common divisor of d and n/d for all positive divisors d of n. Further, let F(k) be the summatory function of f, expressed as F(k) = ∑[f(n) from n=1 to k]. Write a function `calculate_f` that takes an integer k as input and returns F(k).
"""

import math

def calculate_f(k):
    F = 0
    for n in range(1, k+1):
        f_n = 0
        for d in range(1, int(math.sqrt(n)) + 1):
            if n % d == 0:
                f_n += math.gcd(d, n//d)
                if d != n // d:  # Check if divisors are different
                    f_n += math.gcd(n//d, d)
        F += f_n
    return F