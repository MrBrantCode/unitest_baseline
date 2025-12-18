"""
QUESTION:
Create a function called `is_prime` that determines whether a given number is prime or not. Then, use this function to generate a list of all prime numbers between 1000 and 2000 (inclusive), and return the sum of all these prime numbers.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True