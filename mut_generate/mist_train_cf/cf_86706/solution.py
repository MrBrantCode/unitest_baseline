"""
QUESTION:
Write a function called `sum_of_first_n_primes(n)` that takes a positive integer `n` as input and returns the sum of the first `n` prime numbers. The function should not take any other inputs and should handle cases where `n` is 0 or greater than 0.
"""

import math

def sum_of_first_n_primes(n):
    """
    Calculate the sum of the first n prime numbers.

    Args:
    n (int): A positive integer.

    Returns:
    int: The sum of the first n prime numbers.
    """

    sum_of_primes = 0
    count = 0
    num = 2

    while count < n:
        is_prime = True

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            sum_of_primes += num
            count += 1

        num += 1

    return sum_of_primes