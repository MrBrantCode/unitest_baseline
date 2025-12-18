"""
QUESTION:
Implement a function `delete_primes` that takes an array of integers and a number `n` as input, and returns a new array containing all non-prime numbers from 2 to `n` (inclusive). The function should exclude any prime numbers within the range. The array `arr` and the value of `n` are given, but the function should not directly use the array's values. Instead, it should generate the numbers from 2 to `n` and filter out the prime numbers.
"""

import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def delete_primes(n):
    modified_arr = []
    for number in range(2, n+1):
        if not is_prime(number):
            modified_arr.append(number)
    return modified_arr