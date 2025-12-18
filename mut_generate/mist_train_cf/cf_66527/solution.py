"""
QUESTION:
Create a function named `is_prime` that takes an integer as input and returns a boolean value indicating whether the number is prime or not. Then, create a function named `prime_length` that takes a string as input, calculates its length, and returns `True` if the length is a prime number using the `is_prime` function, and `False` otherwise.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_length(string):
    length = len(string)
    return is_prime(length)