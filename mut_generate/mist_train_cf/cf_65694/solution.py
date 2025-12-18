"""
QUESTION:
Create a function `is_prime(number)` that checks if a given number is prime. Use this function in a loop to generate a list of prime numbers from 1 to 100. The list should only include numbers that are prime.
"""

def is_prime(number):
    if number <= 1:  # Primes must be greater than 1
        return False
    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True