"""
QUESTION:
Create a function `isPrime` that checks if a number is prime or not and use the `filter` function to find all prime numbers from the given array [15, 23, 37, 40, 42, 47]. You cannot use any built-in methods or functions to determine if a number is prime.
"""

def isPrime(num):
    # Check if the number is less than 2
    if num < 2:
        return False
    # Check if the number is divisible by any number less than itself
    for i in range(2, num):
        if num % i == 0:
            return False
    return True