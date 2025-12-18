"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given number `n` without using any loops or recursion. The function should return the factorial of `n`.
"""

import math

def factorial(n):
    return math.gamma(n + 1)