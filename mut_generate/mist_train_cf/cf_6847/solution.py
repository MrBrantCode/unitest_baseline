"""
QUESTION:
Write a function `is_prime(n)` that takes a positive integer `n` greater than 1 as input and returns `True` if `n` is a prime number and `False` otherwise. The function should not use any built-in functions or libraries that directly check for prime numbers, and it should have a time complexity of O(sqrt(n)).
"""

def entrance(n):
    if n < 2:
        return False

    # Iterate from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True