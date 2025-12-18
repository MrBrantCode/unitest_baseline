"""
QUESTION:
Write a function `is_prime(n)` that determines whether a given integer `n` is prime. A prime number is an integer greater than 1 that cannot be divided evenly by any integers other than itself and 1.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True