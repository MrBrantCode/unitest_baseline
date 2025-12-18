"""
QUESTION:
Generate a sequence of unique prime numbers within the range of 100 to 200 (inclusive) and return the sequence. The function should be named `is_prime`.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))