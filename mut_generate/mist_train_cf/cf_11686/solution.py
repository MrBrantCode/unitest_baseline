"""
QUESTION:
Write a function `square_of_primes(n)` to generate a list of squares of all prime numbers between 1 and the given number `n`. The function should have a time complexity of O(n*sqrt(k)), where `k` is the largest prime number between 1 and `n`.
"""

import math

def square_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = [x for x in range(1, n + 1) if is_prime(x)]
    return [x**2 for x in primes]