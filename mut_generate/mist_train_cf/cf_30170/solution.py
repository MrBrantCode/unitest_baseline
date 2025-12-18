"""
QUESTION:
Write a function `smallest_prime_replacement(n)` that takes a positive integer `n` as input and returns the smallest prime number that can be obtained by replacing exactly one digit in `n` with any other digit (0-9). If `n` is already a prime number, return `n` itself. Use a helper function `is_prime(x)` to check if a given positive integer `x` is a prime number. The `is_prime(x)` function should return `True` if `x` is prime, and `False` otherwise.
"""

def is_prime(x):
    if x == 2:
        return True
    if x == 1 or x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def smallest_prime_replacement(n):
    if is_prime(n):
        return n
    n_str = str(n)
    for i in range(len(n_str)):
        for j in range(10):
            new_num = int(n_str[:i] + str(j) + n_str[i+1:])
            if is_prime(new_num):
                return new_num
    return None  # No prime number found after replacement