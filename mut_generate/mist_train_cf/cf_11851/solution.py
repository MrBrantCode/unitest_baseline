"""
QUESTION:
Create a function `prime_table(limit)` that prints all prime numbers up to a given `limit`. The function should use a helper function `is_prime(n)` to check if a number is prime. The `is_prime(n)` function should return `False` for numbers less than or equal to 1 and check divisibility up to the square root of `n`.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_table(limit):
    for i in range(2, limit + 1):
        if is_prime(i):
            print(i)