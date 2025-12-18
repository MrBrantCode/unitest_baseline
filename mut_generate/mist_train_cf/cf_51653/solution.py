"""
QUESTION:
Create a regular expression to match strings containing a prime number, specifically single digit primes (2, 3, 5, 7) or prime numbers between 1 and 20 (2, 3, 5, 7, 11, 13, 17, 19).
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_prime_number(n):
    return is_prime(n)