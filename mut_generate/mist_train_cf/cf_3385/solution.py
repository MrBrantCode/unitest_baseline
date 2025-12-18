"""
QUESTION:
Create a function `is_prime(number)` that checks if a given number is prime without using arithmetic or bitwise operators for mathematical operations. Instead, implement a method using logical operators and loops to determine if a number is divisible by another number. The function should return `True` if the number is prime and `False` otherwise.
"""

def is_prime(number):
    if number < 2:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= number:
        if number % i == 0:
            return False
        i += w
        w = 6 - w

    return True