"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` as input and returns `True` if it is prime, `False` otherwise. The function should only consider integers greater than 1 and return `False` for non-prime numbers.
"""

def is_prime(n):
    # Check if the number is less than 2 (not prime)
    if n < 2:
        return False
    
    # Check if the number is divisible by any integer from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # If the number is not divisible by any integer, it is prime
    return True