"""
QUESTION:
Write a function `is_prime(n)` that checks if a number is prime, then write a main function to count the number of prime numbers less than 10000 and return the count as a string with 18 digits, padding with zeros to the left if necessary.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True