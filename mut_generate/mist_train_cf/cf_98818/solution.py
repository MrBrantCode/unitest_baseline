"""
QUESTION:
Write a function called `sigmoid(x)` that takes a number as input and returns the sigmoid of that number. The function should return a value between 0 and 1 for all possible inputs.
"""

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))