"""
QUESTION:
Write a function `find_primes_under(num)` that returns a list of all prime numbers less than the given number `num`. The function should be efficient and only check for factors up to the square root of a number to determine if it is prime.
"""

import math

def find_primes_under(num):
    primes = []
    for potential_prime in range(2, num):
        is_prime = True
        for divisor in range(2, int(math.sqrt(potential_prime)) + 1):
            if potential_prime % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(potential_prime)
    return primes