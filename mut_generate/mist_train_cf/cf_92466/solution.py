"""
QUESTION:
Create a function `find_primes(arr)` that takes an array of integers and returns an array with all the prime numbers in it. The function should handle negative numbers and floating-point numbers correctly by excluding them from the output if they are not prime.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(arr):
    primes = []
    for num in arr:
        if isinstance(num, int) or isinstance(num, float):
            if is_prime(abs(num)):
                primes.append(num)
    return primes