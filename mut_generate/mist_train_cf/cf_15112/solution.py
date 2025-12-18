"""
QUESTION:
Create a function called `is_prime` that takes an integer `n` as input and returns a boolean indicating whether `n` is a prime number or not. The function should handle numbers from 2 onwards and determine primality by checking divisibility up to the square root of `n`.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True