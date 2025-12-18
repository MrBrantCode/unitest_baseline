"""
QUESTION:
Write a function named `prime` that takes an integer `n` as input and returns `True` if the number is prime and `False` otherwise. The function should be efficient and not rely on any external libraries or packages. Use this function to print all prime numbers from 100 to 0.
"""

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2,n):
            if (n % x) == 0:
                return False
        return True