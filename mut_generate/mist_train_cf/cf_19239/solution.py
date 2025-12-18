"""
QUESTION:
Write a function `nth_fibonacci_number(n)` that calculates and returns the Nth Fibonacci number in the Fibonacci sequence. The function should have a time complexity of O(1) and a space complexity of O(1). The input `n` is an integer representing the position of the Fibonacci number to be calculated.
"""

import math

def nth_fibonacci_number(n):
    phi = (1 + math.sqrt(5)) / 2
    fibonacci_number = (phi ** n - (-phi) ** (-n)) / math.sqrt(5)
    return int(fibonacci_number)