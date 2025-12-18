"""
QUESTION:
Create a function `is_prime(n)` that checks whether a number `n` is prime or not. Then, use this function to generate a list of prime numbers from 1 to 1000 and print the list.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True