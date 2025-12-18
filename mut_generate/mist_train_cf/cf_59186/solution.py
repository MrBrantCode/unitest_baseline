"""
QUESTION:
Create a function `get_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the input list. The function should be able to handle any list of integers.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def get_prime_numbers(lst):
    primes = [n for n in lst if is_prime(n)]
    return primes