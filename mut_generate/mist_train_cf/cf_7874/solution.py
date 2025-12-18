"""
QUESTION:
Write a function called `is_prime` that takes a single integer `n` as input. The function should return `True` if `n` is a prime number and `False` otherwise. A prime number is defined as a number greater than 1 that has no positive divisors other than 1 and itself. The function should also return `False` for decimal numbers and negative integers.
"""

def is_prime(n):
    # Check if n is a decimal or negative number
    if n <= 1 or n % 1 != 0:
        return False
    
    # Check if n is divisible by any number from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # n is a prime number
    return True