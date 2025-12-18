"""
QUESTION:
Create a function `product_of_non_repeating_primes(lst)` that takes a list of integers as input and returns the product of all non-repeating prime numbers within the list. The function should be able to handle large numbers and edge cases such as empty or single-element lists.
"""

from functools import reduce
from math import sqrt

def product_of_non_repeating_primes(lst):
    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            for i in range(3, int(sqrt(n))+1, 2):
                if n % i == 0:
                    return False
            return True

    primes = [num for num in set(lst) if is_prime(num)]  
    if not primes:  
        return 0
    else:
        return reduce(lambda x, y: x*y, primes)