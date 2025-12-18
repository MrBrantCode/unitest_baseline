"""
QUESTION:
Write a generator function `prime_in_nested_list` that iterates over a nested list of integers with varying depths and yields the prime numbers found in the list. The function should be able to handle lists nested within other lists and return only the prime numbers. The input list can be of any depth and structure.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_in_nested_list(nested_list):
    for i in nested_list:
        if isinstance(i, list):
            yield from prime_in_nested_list(i)
        elif is_prime(i):
            yield i