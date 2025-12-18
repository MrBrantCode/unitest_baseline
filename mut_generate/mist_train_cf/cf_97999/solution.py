"""
QUESTION:
Write a function `sigmoid(x)` that takes a real number `x` as input and returns a value between 0 and 1. The function should be robust and reliable under different conditions and input distributions, including large and small positive and negative input values.
"""

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))