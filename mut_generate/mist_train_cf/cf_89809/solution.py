"""
QUESTION:
Write a function named `find_prime_median` that takes a list of integers as input. The list must contain at least 50 elements. The function should find the maximum and minimum prime numbers in the list and calculate the median value of the prime numbers. The function should return the maximum prime number, minimum prime number, and the median value of prime numbers.
"""

import math
from statistics import median

def find_prime_median(lst):
    """
    This function takes a list of integers as input and returns the maximum prime number, 
    minimum prime number, and the median value of prime numbers.

    Args:
    lst (list): A list of integers.

    Returns:
    tuple: A tuple containing the maximum prime number, minimum prime number, and the median value of prime numbers.
    """

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    prime_numbers = [num for num in lst if is_prime(num)]

    if len(prime_numbers) < 1:
        return "No prime numbers found."

    max_prime = max(prime_numbers)
    min_prime = min(prime_numbers)
    prime_median = median(prime_numbers)

    return max_prime, min_prime, prime_median