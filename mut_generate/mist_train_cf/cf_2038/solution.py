"""
QUESTION:
Write a function `largest_prime_factor(n)` that takes an integer `n` as input and returns its largest prime factor. The function should handle cases where `n` is not a positive integer by printing an error message and returning. The input number can be up to 10^12.
"""

import math

def largest_prime_factor(n):
    if not isinstance(n, int):
        print("Error: Input must be a valid integer.")
        return
    if n <= 0:
        print("Error: Input must be a positive integer.")
        return

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    largest_factor = None
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i):
                largest_factor = i

            complement = n // i
            if is_prime(complement):
                largest_factor = max(largest_factor, complement) if largest_factor else complement

    return largest_factor if largest_factor else n