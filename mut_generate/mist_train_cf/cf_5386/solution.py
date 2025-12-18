"""
QUESTION:
Write a function named `sum_of_primes` that calculates the sum of all prime numbers between 1 and a given number `n` (exclusive of 2 and 3), using a recursive helper function `is_prime` to check for primality, and optimize it to run in O(sqrt(n)) time complexity. The function `sum_of_primes` should take two optional parameters `i` and `prime_sum` with default values 4 and 0 respectively.
"""

import math

def is_prime(n, i=2):
    if i > math.isqrt(n):
        return True
    if n % i == 0:
        return False
    return is_prime(n, i+1)

def sum_of_primes(n, i=4, prime_sum=0):
    if i > n:
        return prime_sum
    if is_prime(i):
        prime_sum += i
    return sum_of_primes(n, i+1, prime_sum)