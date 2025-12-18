"""
QUESTION:
Create a function named `filter_primes` that takes an array of integers as input and returns a new array containing only the prime numbers from the original array, sorted in ascending order.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(arr):
    return sorted([num for num in arr if is_prime(num)])