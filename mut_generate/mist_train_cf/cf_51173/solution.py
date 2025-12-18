"""
QUESTION:
Implement a function `reverse_display` that takes a list of integers `numbers` with a size between 1 and 10^6. The function should return two separate lists: one containing all prime numbers from `numbers` in reverse order and another containing all non-prime numbers in reverse order. The function should be efficient for large inputs.
"""

import math

def reverse_display(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i*i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    primes = [x for x in reversed(numbers) if is_prime(x)]
    non_primes = [x for x in reversed(numbers) if not is_prime(x)]

    return primes, non_primes