"""
QUESTION:
Write a function `is_prime(n)` that checks if a given number `n` is prime. Then, use this function to find and print all seven-digit prime numbers (from 1,000,000 to 9,999,999).
"""

def is_prime(n):
    if n < 2:
        return False
    for number in itertools.islice(itertools.count(2), int(n**0.5 - 1)):
        if not n % number:
            return False
    return True