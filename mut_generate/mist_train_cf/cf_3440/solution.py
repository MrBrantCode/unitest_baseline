"""
QUESTION:
Create a function named `is_prime` that takes an integer `n` as input and returns `True` if the number is prime and `False` otherwise. The function should be designed to check for primality up to the square root of the input number for efficiency.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True