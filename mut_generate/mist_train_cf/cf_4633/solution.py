"""
QUESTION:
Define a function `is_prime(num)` that takes an integer `num` as input and returns True if `num` is a prime number and False otherwise. Then, create a function `product_of_primes(N)` that takes a positive integer `N` as input and returns the product of the first `N` prime numbers without using any built-in prime number generating functions or libraries.
"""

import math

def product_of_primes(N):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    product = 1
    num = 2

    while count < N:
        if is_prime(num):
            product *= num
            count += 1
        num += 1

    return product