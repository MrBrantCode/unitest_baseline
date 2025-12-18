"""
QUESTION:
Create a function `prime_generator()` that returns an iterable of integers, with each next element being the next prime number. Implement a helper function `is_prime(n: int) -> bool` that checks if a given integer `n` is a prime number, returning `True` if prime and `False` otherwise. The `prime_generator()` function should yield the next prime number each time it is called.
"""

from typing import Iterator

def is_prime(n: int) -> bool:
    """Returns True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator() -> Iterator[int]:
    """Returns an iterable of ints with each next element being the next prime number."""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1