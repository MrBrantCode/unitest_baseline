"""
QUESTION:
Write a function named `is_prime` that takes a single integer `n` as input and returns a boolean indicating whether `n` is a prime number. The function should have a time complexity of O(sqrt(n)) and not use any built-in prime number checking functions or libraries, mathematical formulas, or algorithms commonly used to check for prime numbers.
"""

def is_prime(n):
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