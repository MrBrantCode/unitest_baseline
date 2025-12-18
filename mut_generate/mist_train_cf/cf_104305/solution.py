"""
QUESTION:
Write a function named `sum_of_primes` that takes an array of integers as input and returns the sum of all prime numbers in the array. The function should correctly handle arrays containing non-prime and prime numbers, and it should not include non-prime numbers in the sum.
"""

import math

def sum_of_primes(array):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    sum = 0
    for num in array:
        if is_prime(num):
            sum += num
    return sum