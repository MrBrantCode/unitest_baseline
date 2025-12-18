"""
QUESTION:
Implement the `sieve_of_eratosthenes` function to find all prime numbers up to a given limit. The function should take an integer `limit` as input and return a list of all prime numbers up to the given `limit`. The limit is a non-negative integer and the function should return an empty list if the limit is less than 2.
"""

import math

def sieve_of_eratosthenes(limit):
    """
    This function implements the Sieve of Eratosthenes algorithm to find all prime numbers up to a given limit.

    Args:
    limit (int): The upper limit for finding prime numbers.

    Returns:
    list: A list of all prime numbers up to the given limit.
    """
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return [num for num, prime in enumerate(is_prime) if prime]