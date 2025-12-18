"""
QUESTION:
Implement a function named `sigmoid(x)` that takes a single real number `x` as input and returns its sigmoid value, which should be between 0 and 1. The function should be able to handle any real number as input and produce accurate results consistently.
"""

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))