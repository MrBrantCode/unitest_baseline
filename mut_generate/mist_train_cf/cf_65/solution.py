"""
QUESTION:
Create a function named `triple_primes` that takes a list of integers as input. For each number in the input list, if it is a prime number, triple the number; otherwise, replace it with the sum of the first 10 prime numbers.
"""

import math

def triple_primes(nums):
    """
    This function takes a list of integers, triples the prime numbers, 
    and replaces non-prime numbers with the sum of the first 10 prime numbers.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The modified list of integers.
    """
    first_10_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    prime_numbers = [num for num in nums if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))]

    return [num * 3 if num in prime_numbers else sum(first_10_primes[:10]) for num in nums]