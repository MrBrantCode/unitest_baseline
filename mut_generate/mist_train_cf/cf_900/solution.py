"""
QUESTION:
Create a function `is_triangle_number(num)` that checks if a given integer `num` is a triangle number. A triangle number is a number that can be represented as the sum of consecutive positive integers starting from 1. The function should return `True` if the number is a triangle number and `False` otherwise. The input number will be an integer greater than or equal to 1. The solution must have a time complexity of O(1) and use only constant space, without using any arithmetic operators such as +, -, *, or / to calculate the sum.
"""

import math

def is_triangle_number(num):
    # Calculate the discriminant
    discriminant = 1 + 8 * num
    
    # Check if the discriminant is a perfect square
    if math.isqrt(discriminant) ** 2 == discriminant:
        # Check if the square root of the discriminant minus 1 is divisible by 2
        if (math.isqrt(discriminant) - 1) % 2 == 0:
            return True
    return False