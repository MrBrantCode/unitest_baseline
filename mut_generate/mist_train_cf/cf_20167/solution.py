"""
QUESTION:
Create a function called `find_max_prime_difference` that takes an array of positive integers as input and returns the maximum difference between two prime numbers in the array, along with the two prime numbers that yield this difference. The array is guaranteed to contain at least two prime numbers.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_max_prime_difference(arr):
    primes = [num for num in arr if is_prime(num)]
    max_diff = 0
    prime_1 = None
    prime_2 = None
    
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            diff = primes[j] - primes[i]
            if diff > max_diff:
                max_diff = diff
                prime_1 = primes[i]
                prime_2 = primes[j]
    
    return max_diff, prime_1, prime_2