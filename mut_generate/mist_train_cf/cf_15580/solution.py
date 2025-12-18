"""
QUESTION:
Write a function `is_prime()` that takes an integer as input and returns True if the number is prime, False otherwise. Use this function to find unique prime numbers in a list of strings that represent integers, ignoring case sensitivity and only considering numbers within the range of 1 to 100, inclusive.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True