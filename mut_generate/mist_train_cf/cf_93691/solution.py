"""
QUESTION:
Create a function `prime_fibonacci(n)` that finds the nth Fibonacci number that is also a prime number and calculates the sum of all the prime Fibonacci numbers up to the nth Fibonacci number. The function should not use any built-in libraries for prime number calculation and should have a time complexity of O(n).
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def prime_fibonacci(n):
    count = 0
    sum_prime_fib = 0
    fib = 2
    while count < n:
        if is_prime(fib):
            count += 1
            sum_prime_fib += fib
        fib = fibonacci(fib + 1)
    return fib, sum_prime_fib