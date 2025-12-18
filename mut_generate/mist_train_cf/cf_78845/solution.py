"""
QUESTION:
Write a function `is_prime(n)` to check if a number `n` is prime, and use it to find the sum of all prime numbers in a given array. The function should be optimized to handle large numbers efficiently.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    i = 0
    while (5+i)**2 <= n:
        if n%(5+i) == 0 or n%(7+i) == 0:
            return False
        i += 6
    return True