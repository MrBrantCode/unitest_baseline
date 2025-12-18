"""
QUESTION:
Write a function `is_prime(N)` to check if a given number N is a prime number. The function should return False for N less than 2 and check divisibility up to the square root of N.
"""

def entrance(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True