"""
QUESTION:
Create a function named `remove_duplicates` that takes in a list of positive integers. The function should return a new list containing only the unique prime elements from the input list. The function should exclude any elements that have been encountered before, are not prime, or are divisible by any prime number less than or equal to its square root.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def remove_duplicates(lst):
    unique_primes = []
    encountered = set()
    for num in lst:
        if num in encountered:
            continue
        if is_prime(num):
            unique_primes.append(num)
            encountered.add(num)
    return unique_primes