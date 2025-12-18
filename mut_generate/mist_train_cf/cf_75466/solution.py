"""
QUESTION:
Write a function named `check_prime` that takes an integer as input and returns `True` if the number is prime, and `False` otherwise. Use this function to print all prime numbers in the range from 20 to 50 (inclusive).
"""

def check_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else:
            return True
    else:
        return False