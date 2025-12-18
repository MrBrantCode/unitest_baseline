"""
QUESTION:
Create a function `prime_factors(n)` that calculates and returns the prime factors of a given number `n`. The function should repeatedly divide the input number `n` by the smallest divisor `i` starting from 2, until `n` is no longer divisible by `i`. The function should return a list of prime factors. The input number `n` should be a positive integer greater than 1.
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