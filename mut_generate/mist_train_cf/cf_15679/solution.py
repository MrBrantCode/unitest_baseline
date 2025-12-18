"""
QUESTION:
Generate a list of squares of prime numbers from 0 to 1000. Use a function to determine if a number is prime. The function should return `True` if the number is prime and `False` otherwise. The list should include the squares of all prime numbers in the given range. The function to determine if a number is prime should be named `is_prime(n)` and it should take an integer `n` as input.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def entance():
    primes_squared = []
    for num in range(0, 1001):
        if is_prime(num):
            primes_squared.append(num ** 2)
    return primes_squared