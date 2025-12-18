"""
QUESTION:
Write a lambda function in Python called `std_dev` that takes a list of numbers as input and returns the standard deviation of the numbers. The function should use only built-in Python functions and mathematical formulas. The input list may contain any number of elements.
"""

import math

def std_dev(data):
    return math.sqrt(sum((x - (sum(data) / len(data))) ** 2 for x in data) / len(data))