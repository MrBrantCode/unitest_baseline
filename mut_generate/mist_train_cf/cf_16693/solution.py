"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function should have a time complexity of O(sqrt(n)) and should not use any built-in functions or libraries to check for prime numbers.
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True