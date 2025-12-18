"""
QUESTION:
Create a function called `create_array` that takes a positive integer `n` as input and returns an array of size `n` where all elements are distinct prime numbers. The function should have a time complexity of O(n) and a space complexity of O(n log n).
"""

import math

def create_array(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes