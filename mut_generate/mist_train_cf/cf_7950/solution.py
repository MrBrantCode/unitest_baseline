"""
QUESTION:
Implement a function `sum_of_primes_recursive(n)` that calculates the sum of all prime numbers from 2 to `n` using a recursive approach, with a time complexity of O(sqrt(n)) and using a constant amount of additional space.
"""

import math

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    sqrt_num = math.isqrt(number) + 1
    for i in range(3, sqrt_num, 2):
        if number % i == 0:
            return False
    return True

def find_primes(current_number, n, sum_of_primes):
    if current_number > n:
        return sum_of_primes

    if is_prime(current_number):
        sum_of_primes += current_number

    current_number += 1
    return find_primes(current_number, n, sum_of_primes)

def sum_of_primes_recursive(n):
    return find_primes(2, n, 0)