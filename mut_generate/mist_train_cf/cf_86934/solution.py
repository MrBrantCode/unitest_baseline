"""
QUESTION:
Create a function called `is_prime` to check if a given number is prime and use it to generate a list of the first 100 prime numbers. Calculate the sum of the cubes of these prime numbers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True