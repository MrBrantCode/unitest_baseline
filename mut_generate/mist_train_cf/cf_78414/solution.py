"""
QUESTION:
Write a function `prime_fibonacci(n)` that returns the first `n` prime numbers that are also Fibonacci numbers. The function should use helper functions `is_prime(num)` and `fibonacci(n)` or equivalent logic to check if a number is prime and to generate Fibonacci numbers respectively. The function should not include any unnecessary code or print statements, and should only return the list of prime Fibonacci numbers. Note that generating large Fibonacci numbers can be computationally expensive, so the input `n` should be chosen carefully.
"""

import math

# Check if number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(num)) + 1
    for i in range(3, sqrt_n, 2):
        if num % i == 0:
            return False
    return True

# Calculate Fibonacci numbers
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

def prime_fibonacci(n):
    i = 1
    results = []
    while len(results) < n:
        fib = fibonacci(i)
        if is_prime(fib):
            results.append(fib)
        i += 1
    return results