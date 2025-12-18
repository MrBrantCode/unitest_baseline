"""
QUESTION:
Write a function `countAndSumOfDivisiblePrimes` that takes two parameters, `start` and `end`, representing a range of numbers. The function should generate a series of random prime numbers within this range, count the numbers that are divisible by 3, 5, and 7, and calculate the sum of these numbers. The function should return both the count and the sum of the prime numbers that satisfy the divisibility conditions.
"""

import math
import random

def countAndSumOfDivisiblePrimes(start, end):
    """
    Generate a series of random prime numbers within a given range, 
    count the numbers that are divisible by 3, 5, and 7, 
    and calculate the sum of these numbers.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.

    Returns:
        tuple: A tuple containing the count and sum of prime numbers 
               that are divisible by 3, 5, and 7.
    """

    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    total_sum = 0
    for num in range(start, end + 1):
        if is_prime(num) and num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
            count += 1
            total_sum += num
    return count, total_sum