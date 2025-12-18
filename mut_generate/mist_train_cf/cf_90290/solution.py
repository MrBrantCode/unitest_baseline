"""
QUESTION:
Create a function `remove_duplicates(lst)` that takes a list of positive integers as input, removes duplicates and non-prime numbers, and returns a new list with only the unique prime elements. The function should check each element to see if it has been encountered before and if it is a prime number. If an element has not been encountered before and is a prime number, it should be added to the new list.
"""

import math

def remove_duplicates(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    unique_primes = []
    encountered = set()
    for num in lst:
        if num in encountered:
            continue
        if is_prime(num):
            unique_primes.append(num)
            encountered.add(num)
    return unique_primes