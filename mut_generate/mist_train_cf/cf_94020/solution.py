"""
QUESTION:
Write a function `find_primes(start, end)` that takes two integers `start` and `end` and returns a list of all prime numbers between `start` and `end` (inclusive). The function should have a time complexity of O((end-start+1)*sqrt(end)).
"""

import math

def find_primes(start, end):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes