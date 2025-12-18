"""
QUESTION:
Create a function `nth_fibonacci_number(n)` that calculates the Nth Fibonacci number. The function should achieve a time complexity of O(1) and a space complexity of O(1).
"""

import math

def nth_fibonacci_number(n):
    phi = (1 + math.sqrt(5)) / 2
    fibonacci_number = (phi ** n - (-phi) ** (-n)) / math.sqrt(5)
    return int(fibonacci_number)