"""
QUESTION:
Implement a function `sigmoid(x)` that takes a real number `x` as input and returns a value between 0 and 1. The function should be able to handle inputs of varying ranges and consistently produce accurate results.
"""

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))