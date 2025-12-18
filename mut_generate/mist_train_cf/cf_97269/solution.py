"""
QUESTION:
Implement a function `find_prime_numbers(m, n)` that finds all prime numbers in the range from `m` to `n` (inclusive), where `n - m <= 10^9`. The function should return a list of prime numbers within the given range.
"""

import math

def find_prime_numbers(m, n):
    """
    Finds all prime numbers in the range from m to n (inclusive).
    
    Args:
    m (int): The lower bound number.
    n (int): The upper bound number.
    
    Returns:
    list: A list of prime numbers within the given range.
    """
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False

    return [j for j in range(m, n + 1) if isPrime[j]]