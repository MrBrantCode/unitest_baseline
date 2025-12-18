"""
QUESTION:
Create a function named `fibonacci_primes` that takes an integer `n` as input and returns a list of the first `n` prime numbers found in the Fibonacci series. The function should have a time complexity analysis.
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

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

def fibonacci_primes(n):
    primes = []
    i = 0
    while len(primes) < n:
        fib = fibonacci(i)
        if is_prime(fib):
            primes.append(fib)
        i += 1
    return primes