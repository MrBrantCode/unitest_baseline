"""
QUESTION:
Construct a function `fib_primes(n)` that calculates prime numbers within the Fibonacci sequence that don't exceed the input number `n`. The function should return a list of these prime numbers. Implement an efficient algorithm to check for primality, and optimize the computation for large inputs.
"""

import math

def fib_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    fib = [0, 1]
    while fib[-1] <= n:
        num = fib[-1] + fib[-2]
        if num > n:
            break
        fib.append(num)
    return [num for num in fib[2:] if is_prime(num)]