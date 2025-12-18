"""
QUESTION:
Write a function `magnify_primes(arr)` that takes an array of up to 1000 integers (each integer can be as large as 10^9) and returns a new array where each prime number in the input array is multiplied by 3, and non-prime numbers remain unchanged.
"""

from math import isqrt

def magnify_primes(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    return [num*3 if is_prime(num) else num for num in arr]