"""
QUESTION:
Create a function `get_prime(nums: list) -> list` that takes a list of integers as input and returns a list of prime numbers found in the input list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should only consider numbers greater than 1 as potential prime numbers and should not include 1 in the output list. The function should be optimized by checking divisors up to the square root of each number.
"""

import math

def get_prime(nums: list) -> list:
    primes = []
    for num in nums:
        if num > 1:
            for i in range(2, math.isqrt(num) + 1):  
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes