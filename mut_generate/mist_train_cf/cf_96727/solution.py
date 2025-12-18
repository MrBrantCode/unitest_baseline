"""
QUESTION:
Write a function `find_max_min_median_prime(numbers)` that takes a list of integers `numbers` with at least 20 elements as input and returns the maximum prime number, minimum prime number, and the median of the prime numbers in the list. The function should handle cases where the input list contains no prime numbers.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_max_min_median_prime(numbers):
    primes = [num for num in numbers if is_prime(num)]
    if len(primes) == 0:
        return None
    max_prime = max(primes)
    min_prime = min(primes)
    primes.sort()
    median = primes[len(primes) // 2] if len(primes) % 2 != 0 else (primes[len(primes) // 2 - 1] + primes[len(primes) // 2]) / 2
    return max_prime, min_prime, median