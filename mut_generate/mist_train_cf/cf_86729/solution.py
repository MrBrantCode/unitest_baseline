"""
QUESTION:
Create a function called `calculate_square_root` that takes an integer as input and returns the square root of the number if it is a positive integer between 1 and 100. If the number is not within the valid range, the function should print an error message instead of returning a value.
"""

import math

def calculate_square_root(num):
    if 1 <= num <= 100:
        return math.sqrt(num)
    else:
        print("Error: The number is not within the valid range.")