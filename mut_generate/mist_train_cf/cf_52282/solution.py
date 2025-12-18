"""
QUESTION:
Create two functions: `is_prime(n)` to check if a number `n` is prime, and `prime_length(string)` to check if the length of a given string is a prime number. The function `prime_length(string)` should call `is_prime(n)` to determine if the length of the string is prime. The function `is_prime(n)` should return `True` if the number is prime and `False` otherwise, while the function `prime_length(string)` should also return `True` if the length of the string is prime and `False` otherwise.
"""

def is_prime(n):
    """Check if number is prime or not."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def entrance(s):
    """Check if length of a string is a prime number."""
    length = len(s)
    return is_prime(length)