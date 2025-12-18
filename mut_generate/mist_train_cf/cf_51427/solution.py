"""
QUESTION:
Implement a function named `is_prime` that takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. The function should be optimized for time complexity, ideally achieving a time complexity of less than `O(n)`. The function should be able to handle integers of any size, but should be particularly efficient for large numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True