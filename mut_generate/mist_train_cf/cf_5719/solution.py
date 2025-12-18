"""
QUESTION:
Define a function named `prime_product` that takes two positive prime numbers as input, checks if they are even, converts negative numbers to positive, rounds floating-point numbers to the nearest integer, and returns their product as a string. If the product is a perfect square, the function should return the square root of the product as a string instead. The function should only work for numbers that are both prime and even.
"""

import math

def prime_product(num1, num2):
    # Check if both numbers are positive prime numbers
    if not (is_prime(num1) and is_prime(num2)):
        return "Both numbers should be positive prime numbers."

    # Check if both numbers are even
    if not (num1 % 2 == 0 and num2 % 2 == 0):
        return "Both numbers should be even."

    # Convert negative numbers to positive
    if num1 < 0:
        num1 = abs(num1)
    if num2 < 0:
        num2 = abs(num2)

    # Round floating-point numbers to the nearest integer
    num1 = round(num1)
    num2 = round(num2)

    # Calculate the product
    product = num1 * num2

    # Check if the product is a perfect square
    if math.isqrt(product) ** 2 == product:
        return str(math.isqrt(product))
    else:
        return str(product)

# Helper function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True