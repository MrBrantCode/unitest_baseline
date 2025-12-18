"""
QUESTION:
Create a function `is_prime()` to check if a number is prime, then use this function to create an array of the first 1000 prime numbers. The `is_prime()` function should take an integer as input and return a boolean value indicating whether the number is prime. The array should be populated with the first 1000 prime numbers, starting from the smallest prime number.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True