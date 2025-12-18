"""
QUESTION:
Write a function named `print_primes_in_range` that takes two parameters: `start` and `end`, representing the range of numbers to check for prime numbers. The function should print each prime number in the given range and return the sum of all prime numbers found. The function must iterate over each number in the range and determine whether it is prime by checking for divisibility up to its square root.
"""

import math

def print_primes_in_range(start, end):
    """
    Prints each prime number in the given range and returns the sum of all prime numbers found.

    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (exclusive).

    Returns:
        int: The sum of all prime numbers in the range.
    """
    sum_of_primes = 0
    for num in range(start, end):
        if num > 1:
            is_prime = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num)
                sum_of_primes += num
    return sum_of_primes