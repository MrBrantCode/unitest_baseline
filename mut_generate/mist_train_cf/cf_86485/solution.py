"""
QUESTION:
Write a function `absolute_difference` that takes two numbers `a` and `b` as input and returns their absolute difference rounded to the nearest integer. The function must use basic arithmetic operations and comparisons no more than twice and have a time complexity of O(1) with constant space complexity.
"""

import math

def absolute_difference(a, b):
    difference = a - b
    if difference < 0:
        difference *= -1
    return round(difference)