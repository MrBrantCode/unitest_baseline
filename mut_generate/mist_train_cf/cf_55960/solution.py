"""
QUESTION:
Create a function `odd_primes` that takes two parameters `start` and `end` and prints all odd prime numbers between `start` and `end` (inclusive) using recursion. The function should not use any loops.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n**0.5)+1
    for divisor in range(3, sqrt_n, 2):
        if n % divisor == 0:
            return False
    return True

def odd_primes(start, end):
    if start > end:
        return
    if is_prime(start) and start % 2 != 0:
        print(start)
    return odd_primes(start + 1, end)