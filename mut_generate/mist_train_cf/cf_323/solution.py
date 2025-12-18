"""
QUESTION:
Create a function called `is_prime` that determines if a given input number `n` is a prime number or not. If `n` is a prime number, the function should return `True`. If `n` is not a prime number, the function should return the smallest prime factor of `n`. The function should be able to handle inputs up to 10^12.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return True