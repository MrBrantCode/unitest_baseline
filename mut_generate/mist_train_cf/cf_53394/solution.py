"""
QUESTION:
Create two functions: `is_prime` and `prime_length`. The `is_prime` function should take an integer `n` and return `True` if `n` is a prime number and `False` otherwise. The `prime_length` function should take a string `s` and return `True` if the length of `s` is a prime number, and `False` otherwise. The `prime_length` function should use the `is_prime` function to check if the length of the string is prime.
"""

def is_prime(n):
    if n <= 1:    # prime numbers are greater than 1
        return False
    elif n <= 3:   # 2 and 3 are prime
        return True
    # check for multiples of 2 and 3
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_length(s):
    return is_prime(len(s))