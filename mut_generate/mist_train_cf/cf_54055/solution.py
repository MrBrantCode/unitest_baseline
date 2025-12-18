"""
QUESTION:
Write a function `is_prime(n)` that determines whether a given number `n` is a prime number. The function should return `True` for prime numbers and `False` otherwise. The input `n` is a positive integer.
"""

def is_prime(n):
    if n <= 1: 
        return False  
    if n == 2: 
        return True  
    if n % 2 == 0: 
        return False  
    for i in range(3, int(n**0.5) + 1, 2): 
        if n % i == 0:
            return False  
    return True