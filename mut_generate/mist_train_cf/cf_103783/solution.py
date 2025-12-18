"""
QUESTION:
Create a function named `is_prime` that takes an integer `n` and returns a boolean indicating whether `n` is a prime number or not, excluding 2 and 5. The function should check for primality up to the square root of `n` for efficiency.
"""

def is_prime(n):
    if n < 2 or n == 5:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True