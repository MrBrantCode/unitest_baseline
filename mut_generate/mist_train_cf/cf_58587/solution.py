"""
QUESTION:
Create a function named `largest_prime_factor(n: int)` that takes an integer `n` as input and returns the largest prime factor of `n`. The function should work for both positive and negative integers, assuming `abs(n) > 1` and `n` is not prime. The function should optimize the procedure by only scrutinizing odd factors succeeding 2.
"""

def largest_prime_factor(n: int):
    """Return the largest prime factor of a positive or negative n. Assume abs(n) > 1 and is not prime.
    Optimize the procedure by only scrutinizing odd factors succeeding 2.
    """
    n = abs(n)
    last_factor = 1
    while n % 2 == 0:
        last_factor = 2
        n = n / 2
    factor = 3
    max_factor = n ** 0.5
    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            n = n / factor
            last_factor = factor
            while n % factor == 0:
                n = n / factor
            max_factor = n ** 0.5
        factor += 2
    if n == 1:
        return last_factor
    else:
        return n