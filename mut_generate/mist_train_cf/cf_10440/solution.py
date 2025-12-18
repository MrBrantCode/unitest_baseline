"""
QUESTION:
Create a function `first_n_primes(n)` that generates and returns the first `n` prime numbers, where `n` is a positive integer. The function should take no arguments other than `n`. The prime numbers should be returned in ascending order.
"""

import math

def first_n_primes(n):
    """
    Generates and returns the first n prime numbers.

    Args:
        n (int): A positive integer.

    Returns:
        list: A list of the first n prime numbers in ascending order.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = []
    count = 0
    num = 2

    while count < n:
        if is_prime(num):
            prime_numbers.append(num)
            count += 1
        num += 1

    return prime_numbers