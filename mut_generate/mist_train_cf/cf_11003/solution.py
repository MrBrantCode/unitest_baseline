"""
QUESTION:
Create a function named `create_prime_cubes_dict` that takes an integer `n` as input and returns a dictionary. The dictionary should contain prime numbers between 2 and `n` (inclusive) as keys, and their cubes as corresponding values. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def create_prime_cubes_dict(n):
    prime_cubes = {}
    for num in range(2, n+1):
        if is_prime(num):
            prime_cubes[num] = num ** 3
    return prime_cubes