"""
QUESTION:
Write a function `absolute_difference(a, b)` that calculates the absolute difference between two numbers `a` and `b`, rounds the result to the nearest integer, and returns it. The function should only use basic arithmetic operations (+, -, *, /) and comparisons (<, >, ==) a maximum of two times, have a time complexity of O(1), and use a constant amount of space. The function should be able to handle floating-point numbers as inputs.
"""

import math

def absolute_difference(a, b):
    difference = a - b
    if difference < 0:
        difference *= -1
    return round(difference)