"""
QUESTION:
Generate a function named `is_prime(n)` that checks if a number `n` is prime. Using this function, create a list of 12 unique random prime numbers between 2 and 100 (inclusive) and return them in descending order.
"""

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True