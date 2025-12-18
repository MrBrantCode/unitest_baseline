"""
QUESTION:
Create a function `find_max_min_median_prime` that takes a list of integers as input, filters out non-prime numbers, and returns the maximum prime number, the minimum prime number, and the median of the prime numbers in the list. The input list must contain at least 20 elements. If no prime numbers are found, return a message indicating this.
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
    """
    This function filters out non-prime numbers from the input list, 
    and returns the maximum prime number, the minimum prime number, 
    and the median of the prime numbers in the list.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing the maximum prime number, the minimum prime number, 
        and the median of the prime numbers. If no prime numbers are found, returns a message.
    """
    primes = [num for num in numbers if is_prime(num)]
    if len(primes) == 0:
        return "No prime numbers found."
    max_prime = max(primes)
    min_prime = min(primes)
    primes.sort()
    median = primes[len(primes) // 2] if len(primes) % 2 != 0 else (primes[len(primes) // 2 - 1] + primes[len(primes) // 2]) / 2
    return max_prime, min_prime, median