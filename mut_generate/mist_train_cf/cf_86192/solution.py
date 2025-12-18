"""
QUESTION:
Create a function named `is_prime(n)` that checks if a given number `n` is prime or not, returning "Prime" if it is prime and "Not Prime" otherwise. The function should have a time complexity of O(sqrt(n)) and use constant space. It should handle negative numbers, decimal numbers, and large numbers (greater than 10^9) efficiently, returning "Not Prime" for non-prime inputs.
"""

import math

def entrance(n):
    if n < 2 or not isinstance(n, int):
        return "Not Prime"

    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return "Not Prime"

    return "Prime"