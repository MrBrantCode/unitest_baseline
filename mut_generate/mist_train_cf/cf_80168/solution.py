"""
QUESTION:
Write a function named `cumulative_sum_of_primes` that calculates the cumulative sum of prime numbers that are either one or two units greater than a perfect square and fall within the range of 100 to 200, inclusive. The function should not take any arguments.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def cumulative_sum_of_primes():
    perfect_squares = [i**2 for i in range(11, 15)]
    primes_sum = 0
    for square in perfect_squares:
        candidate1, candidate2 = square + 1, square + 2
        if is_prime(candidate1) and 100 <= candidate1 <= 200:
            primes_sum += candidate1
        if is_prime(candidate2) and 100 <= candidate2 <= 200:
            primes_sum += candidate2
    return primes_sum