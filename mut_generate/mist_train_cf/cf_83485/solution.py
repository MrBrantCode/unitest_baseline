"""
QUESTION:
Write a function `prime_factors(n)` that returns a list of prime factors of a given number `n`. The function should use dynamic programming principles to achieve this. The input number `n` is a positive integer, and the function should return a list of integers representing the prime factors of `n`. The function should not use recursion.
"""

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors