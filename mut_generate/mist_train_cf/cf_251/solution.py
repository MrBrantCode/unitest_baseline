"""
QUESTION:
Create a function `fibonacci(n)` that generates the nth term in the Fibonacci sequence without using recursion or iteration. The function should take an integer `n` as input, where `n` is a positive integer greater than or equal to 1, and return the nth term in the Fibonacci sequence with a time complexity of O(1).
"""

import math

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return int((phi**n - (-phi)**(-n)) / math.sqrt(5))