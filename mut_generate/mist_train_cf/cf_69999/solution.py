"""
QUESTION:
Write a function `is_prime` that checks if a number is prime. Then, create a program that takes a range of integers as input from the user, uses `is_prime` to find all prime numbers within that range, prints those prime numbers, and calculates the prime density by dividing the number of prime numbers by the total numbers in the range. The input range is inclusive. The program should round the prime density to two decimal places.
"""

def is_prime(n):
    """Check if number n is a prime."""
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