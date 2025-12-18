"""
QUESTION:
Write a function called `select_primes` that takes a list of integers and an integer `N` as input, and returns the sum of all prime numbers in the list whose index is a multiple of `N`.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def select_primes(lst, N):
    return sum(num for i, num in enumerate(lst) if i % N == 0 and is_prime(num))