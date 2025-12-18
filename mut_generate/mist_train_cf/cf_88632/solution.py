"""
QUESTION:
Write a function called `prime_sum_product(a, b)` that finds the sum and product of all prime numbers within a given range `[a, b]`. The function should not use any built-in libraries or functions to check for prime numbers and should be optimized to have a time complexity of O(sqrt(n)) where n is the largest number in the range.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def prime_sum_product(a, b):
    prime_sum = 0
    prime_product = 1
    for num in range(a, b+1):
        if is_prime(num):
            prime_sum += num
            prime_product *= num
    return prime_sum, prime_product