"""
QUESTION:
Given a function `is_prime_count`, write an efficient algorithm to verify whether an integer `num` is a prime number and return the count of prime numbers found. The function should optimize for time complexity and have a space complexity of O(1).
"""

import math

def is_prime_count(num):
    primeCount = 0

    if num < 2:
        return primeCount

    if num == 2:
        primeCount += 1
        return primeCount

    if num % 2 == 0:
        return primeCount

    divisor = 3
    sqrt = math.isqrt(num)
    if sqrt * sqrt == num:
        sqrt -= 1

    while divisor <= sqrt:
        if num % divisor == 0:
            return primeCount
        divisor += 2

    primeCount += 1
    return primeCount