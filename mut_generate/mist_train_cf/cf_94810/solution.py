"""
QUESTION:
Write a function named `is_prime` that determines whether a number is prime or not. Then, create a loop to print out all prime numbers from 1000 to 2000, excluding any prime numbers that contain the digit 5. The loop should utilize the `is_prime` function to check for primality.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True