"""
QUESTION:
Write a function named `is_prime` that determines if a given integer `n` is a prime number. The function must not use built-in prime number checking functions, libraries, or common mathematical formulas and algorithms such as the Sieve of Eratosthenes. The function should have a time complexity of O(sqrt(n)).
"""

def entrance(n):
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