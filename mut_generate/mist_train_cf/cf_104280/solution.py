"""
QUESTION:
Create a function `is_prime(n)` that returns a boolean indicating whether the input number `n` is prime or not. The function should be able to handle numbers up to 100. Use this function to generate a list of prime numbers from 1 to 100.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True