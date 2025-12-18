"""
QUESTION:
Write a function named `is_prime` that takes a whole number `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function should exclude even numbers greater than 2 and optimize the computation for time complexity by skipping unnecessary checks. Use this function to print all prime numbers between 0 and 150, inclusive.
"""

def is_prime(n):
    if n <= 1: # numbers less than 2 are not primes
        return False
    if n == 2: # 2 is a prime number
        return True
    if n % 2 == 0: # even numbers greater than 2 are not primes
        return False
    max_div = int(n**0.5) + 1
    for div in range(3, max_div, 2): # skipping even numbers
        if n % div == 0:
            return False
    return True