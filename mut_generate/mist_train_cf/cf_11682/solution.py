"""
QUESTION:
Write a function named `is_prime()` that takes an integer as input and returns a boolean value indicating whether the input is a prime number or not. Then, use a while loop to iterate over all numbers from 2 to a given number (in this case, 100), and print the numbers for which `is_prime()` returns `True`.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True