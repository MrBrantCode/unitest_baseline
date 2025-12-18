"""
QUESTION:
Write a function named `find_next_prime` that takes a positive integer `n` as input, where `n` is less than or equal to 10^6. The function should return a tuple containing a boolean indicating whether `n` is prime and the smallest prime number larger than `n`.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def find_next_prime(n):
    next_prime = n + 1
    while not is_prime(next_prime):
        next_prime += 1
    return (is_prime(n), next_prime)