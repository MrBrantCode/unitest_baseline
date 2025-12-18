"""
QUESTION:
Create a function called `is_prime` that takes an integer as input and returns True if the number is prime, False otherwise. Use this function to generate a sequence of prime numbers less than or equal to 100, starting from 11, using a for loop to iterate over the numbers. The sequence should only include prime numbers.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True