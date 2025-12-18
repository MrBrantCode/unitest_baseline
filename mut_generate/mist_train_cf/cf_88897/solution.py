"""
QUESTION:
Create a function called `prime_numbers_between` that takes two integers `n` and `m`. The function should return a list of prime numbers between `n` and `m` (inclusive), where both `n` and `m` are within the range of -10^9 to 10^9. If `n` or `m` is outside of this range, the function should return an empty list.
"""

import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_between(n, m):
    if abs(n) > 10**9 or abs(m) > 10**9:
        return []
    
    primes = []
    for num in range(n, m + 1):
        if is_prime(num):
            primes.append(num)
    
    return primes