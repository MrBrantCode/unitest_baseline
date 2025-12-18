"""
QUESTION:
Write a function `sum_of_primes(lst)` that calculates the sum of all prime numbers in a given list `lst` without using built-in sum functions or loops, and returns the sum. You can use a helper function if necessary.
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