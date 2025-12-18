"""
QUESTION:
Create a function named `find_primes` that takes an array of integers as input and returns a new array containing only the prime numbers from the original array, sorted in ascending order. The function should have a time complexity of O(n * sqrt(m)), where n is the length of the input array and m is the maximum number in the input array.
"""

import math

def find_primes(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in arr if is_prime(num)]
    primes.sort()
    return primes