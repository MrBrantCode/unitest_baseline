"""
QUESTION:
Create a generator function `prime_generator(n)` that produces prime numbers between `n` squared and two times `n` squared. The function should use a helper function `is_prime(num)` to check if a number is prime. Implement the generator and helper function in Python.
"""

def is_prime(num):
    """Helper function to check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def prime_generator(n):
    """Generator function to produce prime numbers between n squared and two times n squared."""
    for num in range(n*n, 2*n*n):
        if is_prime(num):
            yield num