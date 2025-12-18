"""
QUESTION:
Write a function named `sum_of_primes` that takes two positive integers `lower_limit` and `upper_limit` as input, both greater than 1, and returns the sum of all odd prime numbers between `lower_limit` and `upper_limit` (inclusive).
"""

import math

def sum_of_primes(lower_limit, upper_limit):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    sum = 0
    for num in range(lower_limit, upper_limit + 1):
        if is_prime(num) and num % 2 != 0:
            sum += num
    return sum