"""
QUESTION:
Write a function called `is_prime` that determines whether a given integer is a prime number or not. The function should take an integer as input and return a boolean value indicating whether the number is prime. Assume the input integer is greater than 1.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True