"""
QUESTION:
Write a function `is_prime(n)` that determines whether a given positive integer `n` is prime. The function should return `True` if `n` is prime and `False` otherwise. The time complexity of the function should be O(n^0.5) and the space complexity should be O(1).
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True