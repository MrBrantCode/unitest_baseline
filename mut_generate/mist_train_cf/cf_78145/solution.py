"""
QUESTION:
Write a function `find_primes` that takes a list of integers as input and returns the first five prime numbers found in the list. If there are less than five prime numbers, return all prime numbers found. The function should return a list of integers.
"""

from typing import List

def find_primes(my_list: List[int]) -> List[int]:
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in my_list if is_prime(num)]

    return primes[:5]