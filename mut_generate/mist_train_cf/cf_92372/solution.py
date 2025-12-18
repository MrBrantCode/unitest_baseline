"""
QUESTION:
Write a function named `is_prime` to check if a given number is prime. The function should take an integer as an argument and return `True` if the number is prime and `False` otherwise. A prime number is a whole number greater than 1 that is divisible by only 1 and itself. The function should only check divisibility up to the square root of the number.
"""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True