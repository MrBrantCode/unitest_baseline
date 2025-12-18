"""
QUESTION:
Create a function named `calculate_sum_of_squares` that takes two parameters: a list of numbers and an exponent. The function should calculate the sum of squares of each number raised to the power of the exponent, but only if the exponent is a prime number and the list contains no negative numbers. If the exponent is not a prime number, return the error message "Exponent must be a prime number." If the list contains a negative number, return the error message "Negative numbers are not allowed." The function should assume the exponent is a positive integer.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def calculate_sum_of_squares(numbers, exponent):
    if not is_prime(exponent):
        return "Exponent must be a prime number."

    for number in numbers:
        if number < 0:
            return "Negative numbers are not allowed."

    sum_of_squares = sum([number ** exponent for number in numbers])
    return sum_of_squares