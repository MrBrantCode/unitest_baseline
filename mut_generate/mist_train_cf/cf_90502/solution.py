"""
QUESTION:
Create a function `is_prime_count` that takes an integer `num` as input and returns 1 if the number is prime, otherwise returns 0. The function should not use any loops or conditionals (if, else, while, for, etc.) in its implementation and should have a space complexity of O(1).
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