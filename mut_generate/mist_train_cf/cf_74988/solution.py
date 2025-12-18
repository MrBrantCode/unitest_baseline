"""
QUESTION:
Implement a function `filter_primes` that takes an array of integers as input and returns a new array containing only the prime numbers from the original array. Assume the input array only contains positive integers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(array):
    return [num for num in array if is_prime(num)]