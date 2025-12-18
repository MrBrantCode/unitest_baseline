"""
QUESTION:
Write a function `classify_input(number)` that classifies the input number into one of the following categories: "odd prime", "even prime", "perfect square", "negative prime", or "zero" based on its properties. The function should return "odd prime" if the number is an odd prime number, "even prime" if the number is an even prime number, "perfect square" if the number is a perfect square, "negative prime" if the number is a negative prime number, and "zero" if the number is zero.
"""

import math

def classify_input(number):
    if number == 0:
        return "zero"
    elif number < 0 and is_prime(-number):
        return "negative prime"
    elif is_prime(number):
        if number % 2 == 0:
            return "even prime"
        else:
            return "odd prime"
    elif is_perfect_square(number):
        return "perfect square"
    else:
        return "other"

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def is_perfect_square(number):
    if number < 0:
        return False
    sqrt = int(math.sqrt(number))
    return sqrt*sqrt == number