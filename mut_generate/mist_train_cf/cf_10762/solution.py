"""
QUESTION:
Create a function named `is_prime` that takes an integer as input and returns a boolean indicating whether the number is prime. The function should be able to check for primality by only considering numbers up to the square root of the input number. The `is_prime` function will be used to calculate the sum of all prime numbers in a given range.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True