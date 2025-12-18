"""
QUESTION:
Create a function named "round_to_nearest_whole" that takes a float number as input and returns the nearest whole number. The input number is between -10^9 and 10^9 (inclusive), and the function should handle both positive and negative numbers correctly, including cases where the input is an integer. The function should return the nearest whole number as an integer.
"""

import math

def round_to_nearest_whole(num):
    if num >= 0:
        return math.floor(num) if num - math.floor(num) < 0.5 else math.ceil(num)
    else:
        return math.ceil(num) if num - math.ceil(num) > -0.5 else math.floor(num)