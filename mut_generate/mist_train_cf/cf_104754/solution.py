"""
QUESTION:
Write a function `filter_prime_tuples` that takes a list of tuples as input, and returns a new list that excludes any tuples containing only prime numbers. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should return an empty list if the input list is empty.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime_tuples(tuples_list):
    return [tup for tup in tuples_list if any(not is_prime(num) for num in tup)]