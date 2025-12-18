"""
QUESTION:
Create a function named `calculate_square_root` that takes an integer as input, checks if it is a positive integer between 1 and 100, and returns its square root if valid. If the input number is not within the valid range, the function should return an error message. The function must use the sqrt function from the math module.
"""

import math

def calculate_square_root(num):
    if 1 <= num <= 100:
        return math.sqrt(num)
    else:
        return "Error: The number is not within the valid range."