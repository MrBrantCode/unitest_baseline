"""
QUESTION:
Create a function named `is_prime(n)` that determines whether a given integer `n` is prime or not. Then, use this function to print a 15 by 15 multiplication table that only includes prime numbers. The table should have prime numbers on both the rows and columns, and the products of these prime numbers should be displayed in the table. Non-prime numbers and their products should be represented as empty spaces.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True