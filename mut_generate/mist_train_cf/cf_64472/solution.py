"""
QUESTION:
Create a function named `sum_primes` that takes a list of integers as input and returns the sum of all prime numbers in the list. The function should not take any other parameters.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def sum_primes(numbers):
    return sum(x for x in numbers if is_prime(x))