"""
QUESTION:
Write a function called `sum_primes_in_fibo(n)` that calculates the sum of prime numbers in the Fibonacci series up to the nth term. The function should be optimized to handle large inputs efficiently. The function should take one parameter `n`, an integer representing the nth term of the Fibonacci series. The function should return an integer representing the sum of prime numbers in the Fibonacci series up to the nth term.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def sum_primes_in_fibo(n):
    return sum(x for x in fibonacci(n) if is_prime(x))