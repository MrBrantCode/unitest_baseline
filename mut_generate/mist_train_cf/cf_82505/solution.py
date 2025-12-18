"""
QUESTION:
Implement a function `sum_primes(n)` that calculates the sum of all prime numbers less than a given positive integer `n`. The function should return the total sum. The input `n` is a positive integer, and the function should handle edge cases where `n` is 0 or 1.
"""

def is_prime(num):
    if num < 2:  
        return False
    for i in range(2, num):  
        if num % i == 0:  
            return False
    return True  

def sum_primes(n):
    prime_sum = 0
    for i in range(n):
        if is_prime(i):
            prime_sum += i
    return prime_sum