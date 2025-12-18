"""
QUESTION:
Create a function named `sum_of_primes` that takes an integer `n` as an argument and returns the sum of all prime numbers from 1 to `n`. The time complexity of the function should be O(n√n).
"""

import math

def sum_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    primes = [i for i in range(2, n + 1) if is_prime(i)]
    return sum(primes)