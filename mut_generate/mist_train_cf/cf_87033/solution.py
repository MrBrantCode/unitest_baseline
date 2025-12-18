"""
QUESTION:
Write a function named `is_prime` to check if a given integer `n` is a prime number, and another function named `get_prime_factors` to find its prime factors if it's not prime. The function should handle numbers up to 10^9 and have a time complexity of O(sqrt(n)). If `n` is prime, the `is_prime` function should return True, otherwise, it should return False and the `get_prime_factors` function should return a list of its prime factors.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def get_prime_factors(n):
    prime_factors = []
    
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    
    if n > 2:
        prime_factors.append(n)
    
    return prime_factors