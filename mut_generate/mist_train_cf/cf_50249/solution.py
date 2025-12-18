"""
QUESTION:
Write a function `is_prime` that takes an integer `n` and returns `True` if `n` is prime, and `False` otherwise. Then use this function to create a list of all prime numbers between 20 and 80, and for each prime number, print its prime factors (which should include 1 and the prime number itself) and count the occurrence of each prime factor for the entire list of primes. The function should not take any arguments other than `n`.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True