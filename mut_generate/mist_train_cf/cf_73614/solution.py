"""
QUESTION:
Create a function `prime_factors(n)` that determines the prime factors of a given integer `n` and counts the occurrence of each prime factor. The function should be optimized for both time and space complexity to handle large input numbers up to 10^18. The function should return a dictionary-like object with prime factors as keys and their respective counts as values. The input `n` is a large integer, and the function should only consider positive integer inputs.
"""

from collections import Counter

def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return Counter(factors)