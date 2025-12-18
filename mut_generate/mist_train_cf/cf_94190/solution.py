"""
QUESTION:
Create a function called `is_prime` that takes an integer `x` as input and returns a boolean value indicating whether `x` is a prime number or not. The function should return `True` if `x` is prime and `False` otherwise. Assume that the input `x` is a non-negative integer.
"""

def is_prime(x):
    if x < 2:  # 0 and 1 are not prime numbers
        return False
    for i in range(2, int(x**0.5) + 1):  # check divisibility up to the square root of x
        if x % i == 0:  # if x is divisible by any number, it is not prime
            return False
    return True