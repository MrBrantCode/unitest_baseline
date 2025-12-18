"""
QUESTION:
Write a function `filter_primes` that takes a list of integers as input, filters out all the prime numbers, and returns them in ascending order.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    """
    Filters out all the prime numbers from a given list of integers and returns them in ascending order.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of prime numbers in ascending order.
    """
    primes = [number for number in numbers if is_prime(number)]
    primes.sort()
    return primes