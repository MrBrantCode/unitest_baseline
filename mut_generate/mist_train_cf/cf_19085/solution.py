"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` as input and returns a boolean value indicating whether `n` is a prime number or not. The function should not use any built-in functions or libraries to check if a number is prime, and it should implement the check using bitwise operations or an optimized algorithm. 

The function should be able to handle integers greater than 1.
"""

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True