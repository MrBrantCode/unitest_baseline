"""
QUESTION:
Create a function named `get_prime_factors(n)` that takes an integer `n` as input and returns a list of its prime factors without any repetitions. The list should be in ascending order. The input `n` can be any positive integer, and the function should handle it accordingly.
"""

def get_prime_factors(n):
    i = 2
    factors = []

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in factors: 
                factors.append(i)
    if n > 1 and n not in factors:
        factors.append(n)
    return factors