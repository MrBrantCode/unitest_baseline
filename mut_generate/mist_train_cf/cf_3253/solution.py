"""
QUESTION:
Create a function `calculate_sum_of_squares` that calculates the sum of squares of a list of numbers, where each number is raised to the power of a given exponent. The function should return an error message if any negative number is present in the list. Additionally, the function should check if the exponent is a prime number and only calculate the sum of squares if it is. If the exponent is not a prime number, the function should return an error message stating that the exponent must be a prime number. The input will be a list of integers and a positive integer exponent.
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