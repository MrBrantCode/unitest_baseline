"""
QUESTION:
Create a function named `is_prime` that takes an integer `n` as input, checks if it's prime and not divisible by 2, 3, 5, or 7, and returns the result. Using this function, generate a list of 10 random prime numbers within the range of 0 to 1000.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True