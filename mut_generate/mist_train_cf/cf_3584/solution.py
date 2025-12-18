"""
QUESTION:
Create a function named `is_prime()` to check whether a number is prime or not and generate a list of the first 100 prime numbers, including both odd and even primes, sorted in descending order.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True