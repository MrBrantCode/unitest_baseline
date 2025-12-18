"""
QUESTION:
Write a function called `prime_square_product` that takes a list of integers as input and returns the product of prime numbers that are perfect squares and not divisible by 5.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    sqrt_n = math.isqrt(n)
    return n == sqrt_n * sqrt_n

def prime_square_product(nums):
    """
    This function calculates the product of prime numbers that are perfect squares and not divisible by 5.

    Args:
    nums (list): A list of integers.

    Returns:
    int: The product of prime numbers that are perfect squares and not divisible by 5.
    """
    product = 1
    for num in nums:
        if is_prime(num) and is_perfect_square(num) and num % 5 != 0:
            product *= num
    return product