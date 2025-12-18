"""
QUESTION:
You are given two positive integers `a` and `b` (`a < b <= 20000`). Complete the function which returns a list of all those numbers in the interval `[a, b)` whose digits are made up of prime numbers (`2, 3, 5, 7`) but which are not primes themselves.


Be careful about your timing!


Good luck :)
"""

from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True

def all_dig_prime(n):
    for d in str(n):
        if d not in '2357':
            return False
    return True

def find_non_prime_with_prime_digits(a, b):
    res = []
    for i in range(a, b):
        if all_dig_prime(i) and (not is_prime(i)):
            res.append(i)
    return res