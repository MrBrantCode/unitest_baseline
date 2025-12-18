"""
QUESTION:
Write a function `sum_prime_fibonacci(num)` that calculates the sum of the first `num` prime numbers that are also Fibonacci numbers. 

The function should take an integer `num` as input and return the sum of the first `num` prime Fibonacci numbers. The function should not take any other inputs and should not print any output. 

Note that a prime number is a positive integer that is divisible only by itself and 1, and a Fibonacci number is a positive integer that satisfies the property of being a perfect square if 5 * n^2 + 4 or 5 * n^2 - 4 is a perfect square.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    return math.isqrt(5 * n**2 + 4)**2 == 5 * n**2 + 4 or math.isqrt(5 * n**2 - 4)**2 == 5 * n**2 - 4

def sum_prime_fibonacci(num):
    prime_fibonacci_nums = []
    i = 2
    while len(prime_fibonacci_nums) < num:
        if is_prime(i) and is_fibonacci(i):
            prime_fibonacci_nums.append(i)
        i += 1
    return sum(prime_fibonacci_nums)