"""
QUESTION:
Create a function named `fibonacci` that takes an integer `n` as input and returns the `n`th number in the Fibonacci sequence without using recursion or iteration.
"""

import math

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return int((phi**n - (1-phi)**n) / math.sqrt(5))