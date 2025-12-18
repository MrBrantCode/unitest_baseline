"""
QUESTION:
Create a function `nth_prime` that finds the nth prime number. The function should take an integer `n` as input and return the nth prime number. The function should handle large inputs of `n` and optimize its time complexity by only checking divisors up to the square root of the candidate number.
"""

import math

def nth_prime(n):
    """
    Finds the nth prime number.

    Args:
    n (int): The position of the prime number to find.

    Returns:
    int: The nth prime number.
    """
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if prime > math.sqrt(candidate):
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes[-1]