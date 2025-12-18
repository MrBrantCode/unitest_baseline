"""
QUESTION:
Create a function `is_prime` that takes an integer as input and returns a boolean indicating whether the number is prime. Then, use this function to filter a given list of integers and return a new list containing only the prime numbers from the original list. Do not use any built-in prime number checking functions or libraries.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True