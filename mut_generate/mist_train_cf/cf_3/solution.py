"""
QUESTION:
Write a function named `is_prime(n)` that takes an integer `n` as input and returns "Prime" if `n` is a prime number, and "Not Prime" otherwise. The function should have a time complexity of O(sqrt(n)) and use only constant space. The function should handle negative numbers and decimal numbers as "Not Prime", and it should be able to handle large numbers (greater than 10^9) efficiently.
"""

import math

def is_prime(n):
    # Check if the number is less than 2 or not an integer
    if n < 2 or not isinstance(n, int):
        return "Not Prime"

    # Check if the number is divisible by any integer from 2 to the square root of n
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return "Not Prime"

    return "Prime"