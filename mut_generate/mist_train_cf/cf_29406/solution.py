"""
QUESTION:
Create a function `find_primes(n: int) -> List[int]` that takes an integer `n` as input and returns a list of all prime numbers less than `n`. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should return an empty list if `n` is less than or equal to 1.
"""

from typing import List

def find_primes(n: int) -> List[int]:
    prime_list = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    return prime_list