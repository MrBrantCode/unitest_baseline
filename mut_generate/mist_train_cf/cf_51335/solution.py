"""
QUESTION:
Write a function named `prime_advanced_sum` that takes two positive integers `n` and `k` as input. The function should return the cumulative sum of all `n`-digit prime numbers with a digit sum equating to a prime number and not divisible by 5, excluding numbers with an even count of digits and numbers divisible by `k`.
"""

import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_advanced_sum(n, k):
    lower = 10 ** (n - 1)
    upper = 10 ** n
    return sum(i for i in range(lower, upper) 
               if is_prime(i) and len(str(i)) % 2 != 0 
               and is_prime(sum(int(d) for d in str(i))) 
               and sum(int(d) for d in str(i)) % 5 != 0 
               and i % k != 0)