"""
QUESTION:
Write a function called `multiply` that takes a list of integers as input, multiplies the elements at even indices that are odd, divisible by 3, and have a prime number immediately following in the list (excluding the last number), and returns the product. If no such elements exist, the function should return 1. The input list will not exceed 1000 elements.
"""

from functools import reduce
import math

def multiply(lst):
    def is_prime(n):
        if n < 2:
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

    desired_elements = [num for ind, num in enumerate(lst[:-1]) if ind % 2 == 0 and num % 2 != 0 and num % 3 == 0 and (ind+1 < len(lst) and is_prime(lst[ind+1]))]
    return reduce(lambda a, b: a*b, desired_elements) if len(desired_elements) > 0 else 1