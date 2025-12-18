"""
QUESTION:
Write a function named `find_primes` that finds all prime numbers from 1 to `n` and returns them in descending order. The function should have a time complexity of O(sqrt(n)*log(log(n))) or better.
"""

import math

def find_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        sqrt_num = int(math.sqrt(num)) + 1
        for i in range(3, sqrt_num, 2):
            if num % i == 0:
                return False
        return True

    primes = []
    for num in range(n, 1, -1):
        if is_prime(num):
            primes.append(num)
    return primes