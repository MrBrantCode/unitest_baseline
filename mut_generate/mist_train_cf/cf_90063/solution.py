"""
QUESTION:
Delete all prime numbers from a given list of integers and return the modified list. The function should not use built-in list removal methods and must handle duplicate elements. The input list will always contain at least one element. Implement the function `delete_primes(lst)` where `lst` is the list of integers.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def delete_primes(lst):
    shift = 0
    for i in range(len(lst)):
        if is_prime(lst[i - shift]):
            lst.pop(i - shift)
            shift += 1
    return lst