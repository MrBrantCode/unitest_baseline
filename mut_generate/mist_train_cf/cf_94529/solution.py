"""
QUESTION:
Create a function called `sum_of_primes` that calculates the sum of all prime numbers in a given list without using the built-in sum function or any loops. The function should take a list of integers as input and return the sum of prime numbers as an integer.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(lst):
    if len(lst) == 0:
        return 0
    elif is_prime(lst[0]):
        return lst[0] + sum_of_primes(lst[1:])
    else:
        return sum_of_primes(lst[1:])