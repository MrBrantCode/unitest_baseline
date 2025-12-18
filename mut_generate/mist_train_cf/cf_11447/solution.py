"""
QUESTION:
Write a function `is_prime(num)` that takes an integer as input and returns a boolean indicating whether the number is prime or not. The function should return `False` for numbers less than 2. For numbers 2 and above, it should check divisibility up to the square root of the number.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True