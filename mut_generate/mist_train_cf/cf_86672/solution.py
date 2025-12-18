"""
QUESTION:
Write a function `is_triangle_number(num)` that checks if a given integer `num` greater than or equal to 1 is a triangle number, i.e., a number that can be represented as the sum of consecutive positive integers starting from 1. The function should return `True` if the number is a triangle number and `False` otherwise. The solution should have a time complexity of O(1) and use only constant space, without using arithmetic operators such as +, -, *, or / to calculate the sum.
"""

import math

def is_triangle_number(num):
    discriminant = 1 + 8 * num
    if math.isqrt(discriminant) ** 2 == discriminant and (math.isqrt(discriminant) - 1) % 2 == 0:
        return True
    return False