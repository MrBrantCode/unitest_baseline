"""
QUESTION:
Write a function named `fibonacci(n)` that calculates the nth Fibonacci number in O(1) time complexity. The Fibonacci sequence starts with 0 and 1, where each subsequent number is the sum of the previous two.
"""

import math

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (-phi)**(-n)) / math.sqrt(5))