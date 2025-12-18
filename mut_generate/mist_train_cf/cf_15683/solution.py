"""
QUESTION:
Write a function called `is_prime(n)` that checks if a given positive integer `n` is prime. Use this function to print all prime numbers from 1 to 100, inclusive.
"""

# Function to check if a number is prime
def entrance(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True