"""
QUESTION:
Write a function `prime_divisors_sum(n)` that takes a number `n` as input and returns the sum of the squares of its prime divisors. If `n` itself is a prime number, the sum should be multiplied by 2. The function should be efficient for large inputs and should not use any external libraries.
"""

import math

def prime_divisors_sum(n):
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and is_prime(i):
            while n % i == 0:
                n /= i
                divisors.append(i)
    if is_prime(n):
        divisors.append(n)
        return 2 * sum(map(lambda x: x**2, divisors))
    else:
        return sum(map(lambda x: x**2, divisors))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True