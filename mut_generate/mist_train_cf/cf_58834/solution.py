"""
QUESTION:
Write a function `nth_prime_in_fibonacci(n)` that takes a non-negative integer `n` as input and returns the nth prime number in the Fibonacci sequence. If `n` is less than 1 or no prime number exists at that position in the sequence, the function should return -1. The function should be optimized for efficiency and execution speed.
"""

import math

def nth_prime_in_fibonacci(n):
    if n < 1:
        return -1
    count = 0
    fib1, fib2 = 1, 1
    while True:
        fib1, fib2 = fib2, fib1 + fib2
        if fib2 > 1 and all(fib2 % i != 0 for i in range(2, int(math.sqrt(fib2)) + 1)):
            count += 1
            if count == n:
                return fib2