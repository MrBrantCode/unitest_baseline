"""
QUESTION:
Write a function `is_prime_and_odd(n)` that verifies if a number `n` is both prime and odd. Use this function to find and display all prime numbers that are also odd within the range of 1 to 100 inclusively. Implement the solution using a `for` loop and conditional statements.
"""

def is_prime_and_odd(n):
    if n == 1:
        return False
    if n == 2:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True