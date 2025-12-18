"""
QUESTION:
Create a function `is_strong_prime(num)` that checks whether a number is a strong prime number or not. A strong prime number is greater than 1, not a perfect square, and not a multiple of the first five prime numbers (2, 3, 5, 7, and 11). Do not use any mathematical libraries or built-in functions to check for perfect squares or multiples of prime numbers.
"""

def is_strong_prime(num):
    if num <= 1:
        return False

    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True