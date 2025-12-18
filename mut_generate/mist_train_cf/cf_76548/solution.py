"""
QUESTION:
Write a function named `goldbach` that takes an integer `n` as input and returns `False` if `n` cannot be expressed as the sum of two prime numbers, and `True` otherwise. The input number `n` is an integer greater than or equal to 1. The function should not take any other parameters and should not use any global variables.
"""

def goldbach(n):
    def is_prime(i):
        if i <= 1:
            return False
        elif i <= 3:
            return True
        elif i % 2 == 0 or i % 3 == 0:
            return False
        j = 5
        w = 2
        while j * j <= i:
            if i % j == 0:
                return False
            j += w
            w = 6 - w
        return True

    if n <= 2 or n % 2 != 0:
        return False
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            return True
    return False