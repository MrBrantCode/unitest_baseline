"""
QUESTION:
Create a function `is_prime(n)` to check whether a given number `n` is prime, and use it to generate a list of prime numbers between 1000 and 10000 (inclusive). The prime number checking algorithm should have a time complexity of O(n^2) or better, and it must not rely on any built-in functions or libraries for checking prime numbers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True