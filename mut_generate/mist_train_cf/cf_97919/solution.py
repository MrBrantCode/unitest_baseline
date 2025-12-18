"""
QUESTION:
Write a function `calculate_quadratic_values` that calculates the values of a quadratic function y = Ax^2 + Bx + C for a range of x values from -10 to 10. The coefficients A, B, and C must be between -127 and 127. The function should return the calculated y values in binary format and ensure the execution time is less than 2 seconds.
"""

import random

def calculate_quadratic_values(A, B, C):
    y_values = []
    for x in range(-10, 11):
        y = A * x**2 + B * x + C
        y_values.append(bin(y))
    return y_values

# Example usage:
# A = random.randint(-127, 127)
# B = random.randint(-127, 127)
# C = random.randint(-127, 127)
# print(calculate_quadratic_values(A, B, C))