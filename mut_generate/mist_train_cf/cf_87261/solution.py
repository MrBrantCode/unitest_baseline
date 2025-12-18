"""
QUESTION:
Write a function `largest_prime_factor(n)` to find the largest prime factor of a given integer `n`, where `n` can be up to 10^12. If `n` is not a valid integer, or if `n` is a non-positive integer, the function should print an error message.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_factor(n):
    if not isinstance(n, int):
        print("Error: Input must be a valid integer.")
        return None
    if n <= 0:
        print("Error: Input must be a positive integer.")
        return None

    largest_factor = None
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i):
                largest_factor = max(largest_factor, i) if largest_factor is not None else i

            complement = n // i
            if is_prime(complement):
                largest_factor = max(largest_factor, complement) if largest_factor is not None else complement

    if largest_factor is None:
        largest_factor = n

    return largest_factor