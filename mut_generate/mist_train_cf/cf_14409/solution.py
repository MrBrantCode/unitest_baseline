"""
QUESTION:
Write a function `prime_factors(n)` to compute the prime factors of a given positive integer `n`. The function should return a list of prime factors of `n`. Note that the input `n` is a positive integer greater than 1.
"""

def prime_factors(n):
    """
    Compute the prime factors of a given positive integer n.

    Args:
        n (int): A positive integer greater than 1.

    Returns:
        list: A list of prime factors of n.
    """
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
    return factors