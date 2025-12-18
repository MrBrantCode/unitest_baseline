"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. The function should consider that a prime number is a number greater than 1 that cannot be formed by multiplying two smaller natural numbers. The input integer `n` should be greater than or equal to 1.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True