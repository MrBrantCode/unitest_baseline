"""
QUESTION:
Generate a function `is_prime()` to check if a number is prime and use it to generate a 10x10 multiplication table containing only prime numbers. The table should be formatted in a way that all numbers in the table are aligned properly. The prime numbers used in the table should be distinct.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True